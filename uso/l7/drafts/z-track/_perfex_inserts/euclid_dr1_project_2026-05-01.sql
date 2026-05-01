-- Phase 2: Zenodo audit (4 tasks)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES
('Audit Z0 umbrella for Euclid coverage', 'DOI 10.5281/zenodo.19881689 — check observables vs Euclid product families (MER/PHZ/SHE/SIR/SPE/LE3); document gaps in Z4_euclid_coverage_audit_2026-05-01.md', 3, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project'),
('Audit Z1 Track 0 (PNT) for Euclid coverage', 'DOI 10.5281/zenodo.19904395 — coordinate framework, expected NONE direct relevance, confirm', 2, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project'),
('Audit Z2 Track A for Euclid coverage', 'DOI 10.5281/zenodo.19908184 — KiDS/DES coverage maps to Euclid SHE; document bridge', 3, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project'),
('Audit N/U algebra deposit for Euclid coverage', 'DOI 10.5281/zenodo.17283314 — substrate, expected NONE direct, confirm', 1, NOW(), CURDATE(), '2026-05-08', 1, 1, 25, 'project');

-- Phase 3: Repo walkthrough (7 tasks)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES
('Walk repo: hubble-tensor', 'Catalog all claims; mark Euclid-relevance HIGH/MED/LOW/NONE; check duplicates with other repos', 3, NOW(), '2026-05-08', '2026-05-15', 1, 1, 25, 'project'),
('Walk repo: multiresolution-cosmology', 'Catalog claims; identify S8/H0 predictions for Euclid; review prereg/Zenodo_pre_registration_template.md', 3, NOW(), '2026-05-08', '2026-05-15', 1, 1, 25, 'project'),
('Walk repo: uha', 'Catalog claims; review papers/euclid_inquiry_draft.md; check Z-track readme', 3, NOW(), '2026-05-08', '2026-05-15', 1, 1, 25, 'project'),
('Walk repo: carrier-set', 'RSOS-260797 substrate review; mark cross-references to Z-track', 2, NOW(), '2026-05-15', '2026-05-22', 1, 1, 25, 'project'),
('Walk repo: hubble-tension-resolution', 'Background research; identify what is superseded by Z-track', 1, NOW(), '2026-05-15', '2026-05-22', 1, 1, 25, 'project'),
('Walk repo: nu-algebra', 'Foundation algebra; identify what to cite from Euclid prereg', 1, NOW(), '2026-05-15', '2026-05-22', 1, 1, 25, 'project'),
('Walk repo: cosmological-data', 'Data products; plan Euclid DR1 ingestion structure', 2, NOW(), '2026-05-15', '2026-05-22', 1, 1, 25, 'project');

-- Phase 4: Cross-reference + fold + deprecate (3 tasks)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES
('Build cross-reference matrix', 'Claims x Euclid products x existing preregs; output cross_reference_matrix_2026-05-01.md with check/partial/gap/duplicate cells', 3, NOW(), '2026-05-22', '2026-05-29', 1, 1, 25, 'project'),
('Fold redundant claims', 'Consolidate duplicates identified in cross-ref; pick canonical location; replace duplicates with cross-references; document in fold_and_deprecate_log', 3, NOW(), '2026-05-29', '2026-06-12', 1, 1, 25, 'project'),
('Deprecate superseded fragments', 'Mark hubble-91pct-concordance, hubble-97pct-observer-tensor, etc. as DEPRECATED with replacement pointer; visible markers per feedback_show_failures_publicly', 2, NOW(), '2026-06-12', '2026-06-19', 1, 1, 25, 'project');

-- Phase 5: Z*/Z3 post cool-off updates (2 tasks)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES
('Update Z* with Euclid DR1 reference', 'Wait for 2026-05-02 cool-off clear; add 6-param M1 model + Euclid DR1 timeline + Pathria/Poplawski/Gaztanaga citations + scope honesty for novel synthesis; commit do not deposit', 3, NOW(), '2026-05-02', '2026-05-09', 1, 1, 25, 'project'),
('Z3 decision: keep Omega_m only OR extend to Omega_K', 'Eric decision; if extend: add Euclid Omega_K section; if keep: leave for Z4 to carry Omega_K', 2, NOW(), '2026-05-02', '2026-05-09', 1, 1, 25, 'project');

-- Phase 6: Z4 draft + GATE:OPEN + deposit (4 tasks)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES
('Draft Z4 preregistration v0.1', 'Create Z4_euclid_dr1_preregistration_v0_1_DRAFT.md; mirror Z* structure with 10 sections including 6-param M1, Euclid product mapping, line-177 falsification criterion, publish-failure rule', 3, NOW(), '2026-06-19', '2026-07-17', 1, 1, 25, 'project'),
('Z4 marketing-language audit', 'grep -i revolutionary|Nobel|100%|definitively|groundbreaking; expect zero matches; replace with bounded language', 3, NOW(), '2026-07-17', '2026-07-24', 1, 1, 25, 'project'),
('Z4 GATE:OPEN cycle', 'Generate PDF; print to Phaser-3260 number-up=2; 30-min cool-off minimum; Eric reads and confirms GATE:OPEN per feedback_zenodo_publish_gate', 3, NOW(), '2026-07-24', '2026-07-31', 1, 1, 25, 'project'),
('Z4 Zenodo deposit', 'Mint DOI via Zenodo API; PATCH specific fields not full overwrite; verify HTML/PDF; cross-link from Z0 umbrella description-changelog; hash filename per feedback_artifact_hash_naming', 3, NOW(), '2026-07-31', '2026-08-07', 1, 1, 25, 'project');

-- Phase 7: Pre-DR1 dry runs (3 tasks)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES
('Pipeline dry-run on DESI DR2 + DES Y6', 'Validate Z4 fitting pipeline on existing data; M0 vs M1 likelihood; nuisance-parameter sensitivity report; substrate-independent for DR1 slip risk', 2, NOW(), '2026-08-07', '2026-09-30', 1, 1, 25, 'project'),
('Q2 Euclid rehearsal (June 2026)', 'If Q2 release available: ingest; rehearse masking and catalog interfaces; earlier-stage validation', 2, NOW(), '2026-06-01', '2026-06-30', 1, 1, 25, 'project'),
('Z4 GATE:OPEN final review pre-DR1', 'Two weeks before 2026-10-21: re-confirm Z4 thresholds; lock Bayes-factor cutoffs; freeze nuisance prior choices', 3, NOW(), '2026-10-01', '2026-10-08', 1, 1, 25, 'project');

-- Phase 8: Post-DR1 (3 tasks)
INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES
('Ingest Euclid DR1 LE2/LE3 products', '2026-10-21 release: confirm SHE/PHZ/MER/SIR-SPE catalogs available; LE3 if public; ingest to cosmological-data repo', 3, NOW(), '2026-10-21', '2026-10-28', 1, 1, 25, 'project'),
('Run Z4 likelihood on DR1', 'Fit M0 (LCDM) vs M1 (LCDM+hair) on DR1 + DESI DR2 + DES Y6 + Planck 2018 + Pantheon; compute Bayes factor; check line-177 thresholds', 3, NOW(), '2026-10-28', '2026-11-15', 1, 1, 25, 'project'),
('Publish DR1 first-pass results', 'Per Z4 publish-failure rule: deposit non-detection constraints OR surviving anomalies; either way deposit per feedback_show_failures_publicly', 3, NOW(), '2026-11-15', '2026-12-31', 1, 1, 25, 'project');

SELECT COUNT(*) AS tasks_inserted FROM tbltasks WHERE rel_id = 25 AND rel_type = 'project';
