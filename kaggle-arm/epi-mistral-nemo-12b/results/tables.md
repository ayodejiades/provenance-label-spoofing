# Results tables (written by analysis/01_rates.py)

## False-follow rate, heldout seeds

| condition | mistral-nemo:12b |
|---|---|
| C4 | 0.02 [0.01, 0.05] n=160 |
| C1 | 0.44 [0.36, 0.51] n=160 |
| C0 | 0.00 [0.00, 0.02] n=160 |
| C2 | 0.01 [0.00, 0.03] n=160 |
| C3 | 0.49 [0.42, 0.57] n=160 |
| C5 | 0.98 [0.95, 0.99] n=160 |
| C6 | 0.69 [0.61, 0.75] n=160 |
| C7 | 0.11 [0.07, 0.16] n=160 |
| C8 | 0.00 [0.00, 0.02] n=160 |
| C9 | 0.03 [0.01, 0.06] n=160 |
| C10 | 0.01 [0.00, 0.03] n=160 |
| C11 | 0.41 [0.33, 0.48] n=160 |
| C12 | 0.44 [0.37, 0.52] n=160 |
| C13 | 0.82 [0.76, 0.88] n=160 |
| C14 | 0.41 [0.33, 0.48] n=160 |
| C15 | 0.66 [0.59, 0.73] n=160 |
| C16 | 0.44 [0.36, 0.51] n=160 |

## Paired contrasts (A minus B), heldout seeds

| contrast | A | B | model | difference | 95% CI | p (sign) | p (Holm) | pairs |
|---|---|---|---|---|---|---|---|---|
| pc | C4 | C1 | mistral-nemo:12b | -0.42 | [-0.49, -0.34] | 0.0000 |  | 160 |
| decoy | C3 | C1 | mistral-nemo:12b | +0.06 | [+0.00, +0.12] | 0.1078 |  | 160 |
| label_frame | C12 | C1 | mistral-nemo:12b | +0.01 | [-0.06, +0.07] | 1.0000 |  | 160 |
| h1_honest | C2 | C1 | mistral-nemo:12b | -0.43 | [-0.51, -0.35] | 0.0000 | 0.0000 | 160 |
| h2_metadata_forgery | C5 | C1 | mistral-nemo:12b | +0.54 | [+0.47, +0.62] | 0.0000 | 0.0000 | 160 |
| h3_tag_no_labels | C6 | C1 | mistral-nemo:12b | +0.25 | [+0.19, +0.32] | 0.0000 | 0.0000 | 160 |
| h3_tag_vs_honest | C7 | C2 | mistral-nemo:12b | +0.10 | [+0.06, +0.15] | 0.0000 | 0.0001 | 160 |
| h3_tag_partial | C13 | C12 | mistral-nemo:12b | +0.38 | [+0.31, +0.45] | 0.0000 | 0.0000 | 160 |
| h3_prose_vs_honest | C9 | C2 | mistral-nemo:12b | +0.02 | [+0.00, +0.04] | 0.2500 | 0.5000 | 160 |
| h3_prose_partial | C15 | C12 | mistral-nemo:12b | +0.22 | [+0.15, +0.29] | 0.0000 | 0.0000 | 160 |
| h4_fix_tag_vs_honest | C8 | C7 | mistral-nemo:12b | -0.11 | [-0.16, -0.06] | 0.0000 | 0.0001 | 160 |
| h4_fix_prose_vs_honest | C10 | C9 | mistral-nemo:12b | -0.02 | [-0.04, +0.00] | 0.2500 | 0.5000 | 160 |
| h4_fix_tag_partial | C14 | C13 | mistral-nemo:12b | -0.42 | [-0.50, -0.34] | 0.0000 | 0.0000 | 160 |
| h4_fix_prose_partial | C16 | C15 | mistral-nemo:12b | -0.23 | [-0.29, -0.16] | 0.0000 | 0.0000 | 160 |
| h4_fix_metadata | C11 | C5 | mistral-nemo:12b | -0.57 | [-0.66, -0.49] | 0.0000 | 0.0000 | 160 |
| residual_tag_vs_honest | C8 | C2 | mistral-nemo:12b | -0.01 | [-0.02, +0.00] | 1.0000 |  | 160 |
| residual_prose_vs_honest | C10 | C2 | mistral-nemo:12b | +0.00 | [-0.02, +0.02] | 1.0000 |  | 160 |
| residual_tag_partial | C14 | C12 | mistral-nemo:12b | -0.04 | [-0.10, +0.03] | 0.3269 |  | 160 |
| residual_prose_partial | C16 | C12 | mistral-nemo:12b | -0.01 | [-0.07, +0.07] | 1.0000 |  | 160 |
| residual_metadata | C11 | C12 | mistral-nemo:12b | -0.04 | [-0.10, +0.03] | 0.3269 |  | 160 |

## False-follow rate, dev seeds

| condition | mistral-nemo:12b |
|---|---|
| C4 | 0.04 [0.02, 0.08] n=160 |
| C1 | 0.52 [0.44, 0.59] n=160 |
| C0 | 0.01 [0.00, 0.03] n=160 |
| C2 | 0.04 [0.02, 0.08] n=160 |
| C3 | 0.48 [0.41, 0.56] n=160 |
| C5 | 0.94 [0.90, 0.97] n=160 |
| C6 | 0.72 [0.65, 0.79] n=160 |
| C7 | 0.13 [0.09, 0.19] n=160 |
| C8 | 0.04 [0.02, 0.08] n=160 |
| C9 | 0.07 [0.04, 0.12] n=160 |
| C10 | 0.03 [0.01, 0.07] n=160 |
| C11 | 0.43 [0.36, 0.51] n=160 |
| C12 | 0.53 [0.45, 0.61] n=160 |
| C13 | 0.88 [0.82, 0.92] n=160 |
| C14 | 0.43 [0.36, 0.51] n=160 |
| C15 | 0.78 [0.70, 0.83] n=160 |
| C16 | 0.54 [0.47, 0.62] n=160 |

## Paired contrasts (A minus B), dev seeds

| contrast | A | B | model | difference | 95% CI | p (sign) | p (Holm) | pairs |
|---|---|---|---|---|---|---|---|---|
| pc | C4 | C1 | mistral-nemo:12b | -0.48 | [-0.56, -0.40] | 0.0000 |  | 160 |
| decoy | C3 | C1 | mistral-nemo:12b | -0.04 | [-0.11, +0.04] | 0.4177 |  | 160 |
| label_frame | C12 | C1 | mistral-nemo:12b | +0.01 | [-0.06, +0.08] | 0.8601 |  | 160 |
| h1_honest | C2 | C1 | mistral-nemo:12b | -0.48 | [-0.56, -0.40] | 0.0000 | 0.0000 | 160 |
| h2_metadata_forgery | C5 | C1 | mistral-nemo:12b | +0.42 | [+0.35, +0.51] | 0.0000 | 0.0000 | 160 |
| h3_tag_no_labels | C6 | C1 | mistral-nemo:12b | +0.21 | [+0.14, +0.27] | 0.0000 | 0.0000 | 160 |
| h3_tag_vs_honest | C7 | C2 | mistral-nemo:12b | +0.09 | [+0.05, +0.14] | 0.0001 | 0.0002 | 160 |
| h3_tag_partial | C13 | C12 | mistral-nemo:12b | +0.35 | [+0.28, +0.42] | 0.0000 | 0.0000 | 160 |
| h3_prose_vs_honest | C9 | C2 | mistral-nemo:12b | +0.03 | [-0.01, +0.07] | 0.1797 | 0.1797 | 160 |
| h3_prose_partial | C15 | C12 | mistral-nemo:12b | +0.24 | [+0.17, +0.31] | 0.0000 | 0.0000 | 160 |
| h4_fix_tag_vs_honest | C8 | C7 | mistral-nemo:12b | -0.09 | [-0.14, -0.05] | 0.0001 | 0.0002 | 160 |
| h4_fix_prose_vs_honest | C10 | C9 | mistral-nemo:12b | -0.04 | [-0.07, -0.01] | 0.0312 | 0.0625 | 160 |
| h4_fix_tag_partial | C14 | C13 | mistral-nemo:12b | -0.45 | [-0.53, -0.38] | 0.0000 | 0.0000 | 160 |
| h4_fix_prose_partial | C16 | C15 | mistral-nemo:12b | -0.23 | [-0.30, -0.16] | 0.0000 | 0.0000 | 160 |
| h4_fix_metadata | C11 | C5 | mistral-nemo:12b | -0.51 | [-0.59, -0.44] | 0.0000 | 0.0000 | 160 |
| residual_tag_vs_honest | C8 | C2 | mistral-nemo:12b | +0.00 | [-0.03, +0.03] | 1.0000 |  | 160 |
| residual_prose_vs_honest | C10 | C2 | mistral-nemo:12b | -0.01 | [-0.04, +0.03] | 1.0000 |  | 160 |
| residual_tag_partial | C14 | C12 | mistral-nemo:12b | -0.10 | [-0.16, -0.04] | 0.0015 |  | 160 |
| residual_prose_partial | C16 | C12 | mistral-nemo:12b | +0.01 | [-0.06, +0.09] | 0.8642 |  | 160 |
| residual_metadata | C11 | C12 | mistral-nemo:12b | -0.10 | [-0.16, -0.04] | 0.0015 |  | 160 |

Forged claims left in the text after the fix, dev C10: 160 of 160
Forged claims left in the text after the fix, dev C14: 0 of 160
Forged claims left in the text after the fix, dev C16: 160 of 160
Forged claims left in the text after the fix, dev C8: 0 of 160
Forged claims left in the text after the fix, heldout C10: 160 of 160
Forged claims left in the text after the fix, heldout C14: 0 of 160
Forged claims left in the text after the fix, heldout C16: 160 of 160
Forged claims left in the text after the fix, heldout C8: 0 of 160
