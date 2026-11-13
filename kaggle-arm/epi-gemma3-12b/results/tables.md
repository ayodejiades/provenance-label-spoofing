# Results tables (written by analysis/01_rates.py)

## False-follow rate, heldout seeds

| condition | gemma3:12b |
|---|---|
| C4 | 0.04 [0.02, 0.08] n=160 |
| C1 | 0.51 [0.43, 0.58] n=160 |
| C0 | 0.00 [0.00, 0.02] n=160 |
| C2 | 0.17 [0.12, 0.23] n=160 |
| C3 | 0.51 [0.43, 0.58] n=160 |
| C5 | 0.81 [0.74, 0.86] n=160 |
| C6 | 0.57 [0.50, 0.65] n=160 |
| C7 | 0.23 [0.17, 0.30] n=160 |
| C8 | 0.11 [0.07, 0.16] n=160 |
| C9 | 0.26 [0.19, 0.33] n=160 |
| C10 | 0.07 [0.04, 0.13] n=160 |
| C11 | 0.29 [0.22, 0.36] n=160 |
| C12 | 0.36 [0.29, 0.44] n=160 |
| C13 | 0.56 [0.48, 0.63] n=160 |
| C14 | 0.29 [0.22, 0.36] n=160 |
| C15 | 0.53 [0.45, 0.60] n=160 |
| C16 | 0.36 [0.29, 0.43] n=160 |

## Paired contrasts (A minus B), heldout seeds

| contrast | A | B | model | difference | 95% CI | p (sign) | p (Holm) | pairs |
|---|---|---|---|---|---|---|---|---|
| pc | C4 | C1 | gemma3:12b | -0.47 | [-0.54, -0.39] | 0.0000 |  | 160 |
| decoy | C3 | C1 | gemma3:12b | +0.00 | [-0.04, +0.04] | 1.0000 |  | 160 |
| label_frame | C12 | C1 | gemma3:12b | -0.14 | [-0.21, -0.09] | 0.0000 |  | 160 |
| h1_honest | C2 | C1 | gemma3:12b | -0.34 | [-0.41, -0.26] | 0.0000 | 0.0000 | 160 |
| h2_metadata_forgery | C5 | C1 | gemma3:12b | +0.30 | [+0.23, +0.37] | 0.0000 | 0.0000 | 160 |
| h3_tag_no_labels | C6 | C1 | gemma3:12b | +0.07 | [+0.03, +0.12] | 0.0074 | 0.0148 | 160 |
| h3_tag_vs_honest | C7 | C2 | gemma3:12b | +0.06 | [+0.01, +0.11] | 0.0213 | 0.0213 | 160 |
| h3_tag_partial | C13 | C12 | gemma3:12b | +0.19 | [+0.12, +0.26] | 0.0000 | 0.0000 | 160 |
| h3_prose_vs_honest | C9 | C2 | gemma3:12b | +0.09 | [+0.04, +0.14] | 0.0013 | 0.0039 | 160 |
| h3_prose_partial | C15 | C12 | gemma3:12b | +0.16 | [+0.11, +0.22] | 0.0000 | 0.0000 | 160 |
| h4_fix_tag_vs_honest | C8 | C7 | gemma3:12b | -0.12 | [-0.18, -0.07] | 0.0000 | 0.0001 | 160 |
| h4_fix_prose_vs_honest | C10 | C9 | gemma3:12b | -0.18 | [-0.24, -0.12] | 0.0000 | 0.0000 | 160 |
| h4_fix_tag_partial | C14 | C13 | gemma3:12b | -0.27 | [-0.34, -0.20] | 0.0000 | 0.0000 | 160 |
| h4_fix_prose_partial | C16 | C15 | gemma3:12b | -0.17 | [-0.23, -0.11] | 0.0000 | 0.0000 | 160 |
| h4_fix_metadata | C11 | C5 | gemma3:12b | -0.52 | [-0.59, -0.44] | 0.0000 | 0.0000 | 160 |
| residual_tag_vs_honest | C8 | C2 | gemma3:12b | -0.06 | [-0.11, -0.03] | 0.0063 |  | 160 |
| residual_prose_vs_honest | C10 | C2 | gemma3:12b | -0.09 | [-0.14, -0.05] | 0.0003 |  | 160 |
| residual_tag_partial | C14 | C12 | gemma3:12b | -0.07 | [-0.13, -0.03] | 0.0075 |  | 160 |
| residual_prose_partial | C16 | C12 | gemma3:12b | -0.01 | [-0.06, +0.04] | 1.0000 |  | 160 |
| residual_metadata | C11 | C12 | gemma3:12b | -0.07 | [-0.13, -0.03] | 0.0075 |  | 160 |

## False-follow rate, dev seeds

| condition | gemma3:12b |
|---|---|
| C4 | 0.06 [0.03, 0.10] n=160 |
| C1 | 0.46 [0.39, 0.54] n=160 |
| C0 | 0.00 [0.00, 0.02] n=160 |
| C2 | 0.15 [0.10, 0.21] n=160 |
| C3 | 0.44 [0.37, 0.52] n=160 |
| C5 | 0.74 [0.66, 0.80] n=160 |
| C6 | 0.57 [0.50, 0.65] n=160 |
| C7 | 0.26 [0.20, 0.34] n=160 |
| C8 | 0.11 [0.07, 0.17] n=160 |
| C9 | 0.26 [0.19, 0.33] n=160 |
| C10 | 0.09 [0.06, 0.15] n=160 |
| C11 | 0.26 [0.20, 0.34] n=160 |
| C12 | 0.29 [0.23, 0.37] n=160 |
| C13 | 0.61 [0.53, 0.68] n=160 |
| C14 | 0.26 [0.20, 0.34] n=160 |
| C15 | 0.63 [0.55, 0.70] n=160 |
| C16 | 0.41 [0.33, 0.48] n=160 |

## Paired contrasts (A minus B), dev seeds

| contrast | A | B | model | difference | 95% CI | p (sign) | p (Holm) | pairs |
|---|---|---|---|---|---|---|---|---|
| pc | C4 | C1 | gemma3:12b | -0.41 | [-0.48, -0.33] | 0.0000 |  | 160 |
| decoy | C3 | C1 | gemma3:12b | -0.02 | [-0.07, +0.03] | 0.6476 |  | 160 |
| label_frame | C12 | C1 | gemma3:12b | -0.17 | [-0.24, -0.11] | 0.0000 |  | 160 |
| h1_honest | C2 | C1 | gemma3:12b | -0.31 | [-0.38, -0.24] | 0.0000 | 0.0000 | 160 |
| h2_metadata_forgery | C5 | C1 | gemma3:12b | +0.28 | [+0.20, +0.35] | 0.0000 | 0.0000 | 160 |
| h3_tag_no_labels | C6 | C1 | gemma3:12b | +0.11 | [+0.06, +0.17] | 0.0000 | 0.0000 | 160 |
| h3_tag_vs_honest | C7 | C2 | gemma3:12b | +0.11 | [+0.07, +0.16] | 0.0000 | 0.0000 | 160 |
| h3_tag_partial | C13 | C12 | gemma3:12b | +0.31 | [+0.24, +0.39] | 0.0000 | 0.0000 | 160 |
| h3_prose_vs_honest | C9 | C2 | gemma3:12b | +0.11 | [+0.06, +0.16] | 0.0000 | 0.0000 | 160 |
| h3_prose_partial | C15 | C12 | gemma3:12b | +0.34 | [+0.26, +0.41] | 0.0000 | 0.0000 | 160 |
| h4_fix_tag_vs_honest | C8 | C7 | gemma3:12b | -0.15 | [-0.21, -0.09] | 0.0000 | 0.0000 | 160 |
| h4_fix_prose_vs_honest | C10 | C9 | gemma3:12b | -0.16 | [-0.22, -0.11] | 0.0000 | 0.0000 | 160 |
| h4_fix_tag_partial | C14 | C13 | gemma3:12b | -0.34 | [-0.42, -0.27] | 0.0000 | 0.0000 | 160 |
| h4_fix_prose_partial | C16 | C15 | gemma3:12b | -0.23 | [-0.29, -0.16] | 0.0000 | 0.0000 | 160 |
| h4_fix_metadata | C11 | C5 | gemma3:12b | -0.47 | [-0.55, -0.39] | 0.0000 | 0.0000 | 160 |
| residual_tag_vs_honest | C8 | C2 | gemma3:12b | -0.04 | [-0.07, -0.01] | 0.0312 |  | 160 |
| residual_prose_vs_honest | C10 | C2 | gemma3:12b | -0.06 | [-0.10, -0.01] | 0.0225 |  | 160 |
| residual_tag_partial | C14 | C12 | gemma3:12b | -0.03 | [-0.08, +0.01] | 0.3018 |  | 160 |
| residual_prose_partial | C16 | C12 | gemma3:12b | +0.11 | [+0.06, +0.17] | 0.0009 |  | 160 |
| residual_metadata | C11 | C12 | gemma3:12b | -0.03 | [-0.08, +0.01] | 0.3018 |  | 160 |

Forged claims left in the text after the fix, dev C10: 160 of 160
Forged claims left in the text after the fix, dev C14: 0 of 160
Forged claims left in the text after the fix, dev C16: 160 of 160
Forged claims left in the text after the fix, dev C8: 0 of 160
Forged claims left in the text after the fix, heldout C10: 160 of 160
Forged claims left in the text after the fix, heldout C14: 0 of 160
Forged claims left in the text after the fix, heldout C16: 160 of 160
Forged claims left in the text after the fix, heldout C8: 0 of 160
