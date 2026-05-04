-- Register audit file in Perfex
INSERT INTO tblproject_files (file_name, original_file_name, subject, description, filetype, dateadded, project_id, visible_to_customer, staffid, contact_id) VALUES
('external_iid_audit_2026-05-01.md', 'external_iid_audit_2026-05-01.md', 'External IID verification audit 2026-05-01', 'Contradiction-by-merit audit from external IID. Identifies 9 critical/high artifact gaps. Layer 3 proxy validated (DESI 0.289 PASS, Planck 0.315 FAIL). Reproducible 4.89-sigma baseline tension confirmed.', 'text/markdown', NOW(), 25, 0, 1, 0);

-- New tasks from audit (some may overlap existing; described as audit-grade specificity)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES

-- CRITICAL: Euclid v2 payload recovery
('CRITICAL: Recover Euclid v2 deposit payloads from Zenodo DOI 19800601', 'External IID audit 2026-05-01: Zenodo lists 4 files but local workspace has only the MD. Download from Zenodo: (1) EUCLID_PRE_REGISTRATION_v2.pdf, (2) uha_normalization_joint_refit.py, (3) uha_normalization_joint_refit_results.json. Verify md5 against Zenodo manifest. Place in /scratch/repos/uha/papers/euclid_v2/ with hash-named filenames. Single highest-value unblocker per audit.', 4, NOW(), CURDATE(), '2026-05-05', 1, 1, 25, 'project'),

-- CRITICAL: MN-26-1108-L equations
('CRITICAL: Recover MN-26-1108-L Layer 2 source equations', 'External IID audit: Layer 2 delta_r reproduction blocked because MN-26-1108-L manuscript referenced (Zenodo concept 19655902, version 19703045) but absent from local workspace. Either (a) download manuscript PDF/MD/TeX from Zenodo, OR (b) write a faithful helper script layer2_shared_factor.py with unit tests reproducing the delta = delta_alpha + delta_r decomposition. Commit no-free-parameter test.', 4, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project'),

-- HIGH: Z0 v1.2-hybrid recovery
('HIGH: Download exact Z0 v1.2-hybrid deposited files', 'External IID audit: workspace has v1.1 MD and predeposit Z0_final.pdf draft, NOT the deposited v1.2 files at DOI 10.5281/zenodo.19881689. Download Z0_umbrella_preregistration_v1.2_hybrid_d842691.md and .pdf; verify md5; place in /scratch/repos/uha/papers/z0_umbrella/. Restores deposit-chain traceability.', 3, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project'),

-- HIGH: Z2 capture
('HIGH: Capture Z2 Track A DOI and download payloads', 'External IID audit: Z2 metadata exists in pasted-text summary (uploaded 2026-04-30) but DOI not captured locally and no payload present. We have DOI 10.5281/zenodo.19908184 from our earlier audit -- download MD + PDF, verify hashes, place alongside Z0/Z1 in deposit-chain location.', 3, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project'),

-- HIGH: Native-O(1) benchmark bundle
('HIGH: Download complete Native-O(1) benchmark bundle from Zenodo 19702036', 'External IID audit: only .sha256 stub local (bc132e04...). Bundle should contain: prereg, source code, results JSON, run log, manifest, report. Download all from Zenodo, verify against stub hash, place in /scratch/repos/native-o1-benchmark/ with full provenance.', 3, NOW(), CURDATE(), '2026-05-15', 1, 1, 25, 'project'),

-- Reproduction tests as discrete tasks
('Implement hash test: every deposited file matches recorded digest', 'External IID audit recommended unit test: pytest tests/test_hash_manifest.py asserting every local Zenodo deposit file SHA-256 matches the deposit manifest. Catches silent file replacement or partial download.', 2, NOW(), '2026-05-08', '2026-05-15', 1, 1, 25, 'project'),

('Implement Layer 2 identity test', 'External IID audit recommended unit test: pytest tests/test_layer2_identity.py asserting delta_alpha + delta_r == delta numerically across reference cases. Confirms the symbolic decomposition is exact, not fitted.', 2, NOW(), '2026-05-08', '2026-05-22', 1, 1, 25, 'project'),

('Implement no-free-parameter test for Layer 2', 'External IID audit: Layer 2 script must expose NO tunable fit constants. pytest tests/test_layer2_no_free_parameters.py inspects the script for parameter dictionaries / argparse / numerical constants in cancellation logic.', 2, NOW(), '2026-05-08', '2026-05-22', 1, 1, 25, 'project'),

('Implement Layer 3 band test', 'External IID audit recommended unit test: pure function omega_m_band_test(omega_m) returning PASS / MARGIN / FAIL according to [0.282, 0.302] pass band, [0.275, 0.310] fail bounds. pytest tests/test_omega_band.py.', 2, NOW(), '2026-05-08', '2026-05-15', 1, 1, 25, 'project'),

('Implement joint-refit regression test', 'External IID audit: re-run uha_normalization_joint_refit.py and assert posterior summary matches deposited results JSON within tolerance. Requires Euclid v2 payloads first (see CRITICAL task above).', 2, NOW(), '2026-05-15', '2026-06-05', 1, 1, 25, 'project'),

('Implement synthetic Euclid mock for pre-DR1 dry runs', 'External IID audit: when Euclid DR1 absent, run LABELED proxy cases against synthetic mocks (DESI DR2-like baseline, varied Omega_m within band edges) rather than silently substituting public data. pytest tests/test_synthetic_mock.py with explicit MOCK_DATA flag.', 2, NOW(), '2026-05-15', '2026-06-12', 1, 1, 25, 'project'),

-- Documentation discipline
('Document Hubble-claim stratification: 91% baseline + retracted higher claims', 'External IID audit: workspace has 91% reduction as authoritative validated baseline, but 97.x-100% claims described as retracted/archived/synthetic/unverified/walked-back. Co-locate exact deposited payloads with the drafts they supersede. Mark walked-back files visibly. Treat 91% as canonical until exact supporting artifacts are supplied for stronger claims.', 3, NOW(), CURDATE(), '2026-05-22', 1, 1, 25, 'project'),

('Co-locate canonical deposits with superseded drafts', 'External IID audit: until exact deposited payloads sit alongside drafts they supersede, citation-error risk persists (someone grabs walked-back file as if validated). Per repo: identify canonical deposit, place in canonical/ subdirectory; move drafts to drafts/ or archive/; visible README pointing to canonical version.', 2, NOW(), '2026-05-15', '2026-06-05', 1, 1, 25, 'project'),

-- Reproduce-the-reproducible immediately
('Reproduce 4.89-sigma literature baseline tension', 'External IID audit reproduced this in-workspace: SH0ES 73.04 +/- 1.04 vs Planck 2018 67.4 +/- 0.5 -> sqrt((73.04-67.4)^2 / (1.04^2 + 0.5^2)) ~= 4.89-sigma. Lock as the baseline that Layer 2 must structurally decompose. Save as /scratch/repos/hubble-tensor/research/baseline_4.89sigma_2026-05-01.md.', 1, NOW(), CURDATE(), '2026-05-05', 1, 1, 25, 'project'),

('Reproduce Layer 3 band test against current public data', 'External IID audit reproduced: DESI DR2 Omega_m = 0.289 +/- 0.007 lands inside Euclid v2 pass band [0.282, 0.302] -> PASS proxy. Planck 2018 Omega_m = 0.315 +/- 0.007 above 0.310 -> FAIL proxy. Demonstrates band rule is non-vacuous. Save as /scratch/repos/hubble-tensor/research/layer3_proxy_band_test_2026-05-01.md.', 1, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project');

SELECT COUNT(*) AS total_tasks, (SELECT COUNT(*) FROM tblproject_files WHERE project_id = 25) AS total_files FROM tbltasks WHERE rel_id = 25 AND rel_type = 'project';
