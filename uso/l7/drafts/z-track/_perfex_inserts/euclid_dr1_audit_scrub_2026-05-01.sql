INSERT INTO tbltasks (name, description, priority, dateadded, startdate, duedate, addedfrom, status, rel_id, rel_type) VALUES

-- A. Pantheon+ data release
('Clone PantheonPlusSH0ES DataRelease from GitHub + verify hashes', 'IID prediction framework audit identifies PantheonPlusSH0ES GitHub DataRelease as required for joint-refit reproduction. Clone https://github.com/PantheonPlusSH0ES/DataRelease into /scratch/repos/cosmological-data/pantheon-plus-shoes/ ; compute SHA-256 manifest; verify against published checksums where available; record manifest.sha256 alongside the data.', 3, NOW(), CURDATE(), '2026-05-15', 1, 1, 25, 'project'),

-- B. BOSS data
('Add BOSS / legacy BAO datasets to cosmology data pipeline', 'IID prediction framework audit notes BOSS / legacy BAO sets are "public in principle but not re-verified directly" -- should be added next. Pull BOSS DR12 BAO results, eBOSS DR16 LRG/QSO BAO, and earlier 2dFGRS where applicable; place in /scratch/repos/cosmological-data/boss-bao/ with hash manifest. Cross-checks for Z3 Omega_m unification.', 2, NOW(), '2026-05-15', '2026-06-05', 1, 1, 25, 'project'),

-- C. Q1 NOW rehearsal (separate from Q2)
('Euclid Q1 tooling/schema rehearsal NOW (Q1 public since 2025-03-19)', 'IID prediction framework audit: Euclid Q1 has been public since 2025-03-19, useful for tooling and schema rehearsal even though it is NOT DR1 adjudication. Pull Q1 ERO products, exercise MER/PHZ/SHE/SIR-SPE catalog readers, build pipeline scaffolding before Q2 (2026-06-24) and DR1 (2026-10-21). DO NOT use Q1 to adjudicate predictions -- explicitly labeled rehearsal-only.', 2, NOW(), CURDATE(), '2026-06-01', 1, 1, 25, 'project'),

-- D. Walked-back file deprecation verification
('Verify visible WALKED-BACK marker on hubble-tension-dissolution file', 'IID prediction framework audit flags 2026-04-26-hubble-tension-dissolution-WALKED-BACK-NOT-CORRECT.md as exploratory derivation source, not canonical evidence. Verify the file has a top-of-document DEPRECATED/WALKED-BACK header (not just filename). Check all repos referencing it have visible "do not cite as result" notes per feedback_show_failures_publicly.md. Lock the H_0(Omega_m) = 100*sqrt(omega_m/Omega_m) bridge as exploratory bridge ONLY.', 2, NOW(), CURDATE(), '2026-05-22', 1, 1, 25, 'project');

SELECT COUNT(*) AS total_tasks FROM tbltasks WHERE rel_id = 25 AND rel_type = 'project';
