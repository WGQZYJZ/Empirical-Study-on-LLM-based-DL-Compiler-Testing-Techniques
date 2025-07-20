A = torch.rand(10, 10)
A = A.mm(A.t())
(eig_vals, eig_vecs) = torch.linalg.eigh(A)