A = torch.randn(3, 3)
A_sym = ((A + A.t()) / 2)
eigvals = torch.linalg.eigvalsh(A_sym)
(eigvals_sorted, perm) = torch.sort(eigvals)
A_sym_sorted = A_sym[perm, :][:, perm]