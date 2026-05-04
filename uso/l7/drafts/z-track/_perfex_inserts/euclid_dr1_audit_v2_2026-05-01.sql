-- Register file
INSERT INTO tblproject_files (file_name, original_file_name, subject, description, filetype, dateadded, project_id, visible_to_customer, staffid, contact_id) VALUES
('euclid_dr1_verification_audit_v2_2026-05-01.md', 'euclid_dr1_verification_audit_v2_2026-05-01.md', 'External IID audit v2 (byte-verified)', 'Sharper than v1 audit. Byte-verified hash matches on A6 PDF (md5 fc33ee64) and Euclid v2 MD (md5 c2d3de9e). 2 NEW DOIs found: 19361407 (xi-normalization DR2 prediction with code) and 19304441 (Paper 2). Synthetic mock sensitivity table. 4 sensitivity axes: covariance, sample-def drift, concept-vs-version DOI, status-label drift.', 'text/markdown', NOW(), 25, 0, 1, 0);

-- 7 NEW tasks (genuinely new vs v1 audit + assigned to Eric)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES

-- 1. New DOI: xi-normalization DR2 prediction record (HAS code locally we can use as proxy)
('Recover Zenodo DOI 19361407: xi-normalization DR2 prediction record', 'Audit v2 found NEW DOI we did not have in inventory. Record contains bao_desi_dr2.py (Python script with DESI DR2 BAO consensus + 13x13 covariance matrix) and desi_dr2_prediction_record.md. Best-fit Omega_m = 0.290 vs DESI DR2 0.289 +/- 0.007. Strong proxy artifact for pre-DR1 stress tests. Download and verify md5 against record.', 3, NOW(), CURDATE(), '2026-05-15', 1, 1, 25, 'project'),

-- 2. New DOI: Paper 2
('Resolve Zenodo DOI 19304441: Paper 2 (referenced by 19361407)', 'Audit v2 names this DOI as referenced by 19361407. Title and payload list unresolved in audit. Pull metadata, identify what paper this is, decide if it is canonical for our chain.', 1, NOW(), CURDATE(), '2026-05-22', 1, 1, 25, 'project'),

-- 3. Concept-DOI vs version-DOI pin
('Pin MN-26-1108-L version DOI 19703045 in source manifest', 'Audit v2 reproducibility risk: Euclid v2 cites concept DOI 19655902 (auto-resolves to latest revision) AND version DOI 19703045 (pinned r2 manuscript). Source manifest must pin version DOI for byte-exact rerun; concept DOI stays in prose as living pointer. Prevents equation-set drifting underfoot.', 3, NOW(), '2026-05-08', '2026-05-22', 1, 1, 25, 'project'),

-- 4. Hash manifest test with byte-verified assertions
('Implement test_hash_manifest with audit-v2 byte assertions', 'Audit v2 provides specific md5 hashes for 2 byte-verified deposits. pytest tests/test_hash_manifest.py asserting: md5(01_euclid_v2_pre_registration.md) == c2d3de9e32ce014e505bcb786e5c2675; md5(a6_implicitness_zero_parity_pre_registration_2026-04-23.pdf) == fc33ee64d34b99d8361cd59085268ec9. Add Z0 v1.1 SHA-256 b308b3a6... and Z1 SHA-256 89e809b2... assertions.', 3, NOW(), CURDATE(), '2026-05-15', 1, 1, 25, 'project'),

-- 5. Covariance treatment audit
('Audit: covariance treatment in Layer 2 / joint-refit pipelines', 'Audit v2 sensitivity axis #1: DESI cosmology chains and Pantheon+SH0ES covariances must NOT be silently diagonalized. Audit any rerun for full-covariance preservation. Add unit test: load Pantheon+ covariance, assert non-zero off-diagonals, assert pipeline reads them.', 2, NOW(), '2026-05-15', '2026-06-05', 1, 1, 25, 'project'),

-- 6. Sample-definition drift documentation
('Document Euclid v2 sample-definition fallback (3x2pt vs BAO-ladder)', 'Audit v2 sensitivity axis #2: Euclid v2 prereg allows weak-lensing+clustering 3x2pt H_0-equivalent OR BAO-ladder fallback if 3x2pt not in DR1. Both preregistered. Document the fallback explicitly in any results note: evidential meaning is NOT identical. Surface visibly which one is actually used post-DR1.', 2, NOW(), '2026-05-15', '2026-05-29', 1, 1, 25, 'project'),

-- 7. Synthetic mock with audit-v2 specific numbers
('Implement synthetic Euclid mock with audit-v2 sensitivity table', 'Audit v2 provides exact synthetic numbers under fixed omega_m = 0.143 bridge. Implement scripts/synthetic_euclid_mock.py with cases: 0.282 -> 71.21 -> 1.31 sigma; 0.289 -> 70.34 -> 1.97 sigma; 0.292 -> 69.98 -> 2.24 sigma; 0.302 -> 68.81 -> 3.16 sigma; 0.306 -> 68.36 -> 3.52 sigma. KEY FINDING: pass band is NOT uniform in Layer 2 burden -- lower end mild, upper end requires substantial residual compression. Document explicitly.', 3, NOW(), '2026-05-22', '2026-06-12', 1, 1, 25, 'project');

-- Assign all new tasks to Eric (staffid 1)
INSERT INTO tbltask_assigned (staffid, taskid, assigned_from, is_assigned_from_contact)
SELECT 1, t.id, 1, 0
FROM tbltasks t
WHERE t.rel_id = 25 AND t.rel_type = 'project'
  AND t.dateadded > DATE_SUB(NOW(), INTERVAL 2 MINUTE)
  AND NOT EXISTS (
    SELECT 1 FROM tbltask_assigned a WHERE a.taskid = t.id AND a.staffid = 1
  );

SELECT COUNT(*) AS total_tasks, (SELECT COUNT(*) FROM tblproject_files WHERE project_id = 25) AS total_files FROM tbltasks WHERE rel_id = 25 AND rel_type = 'project';
