A = torch.randn(3, 5)
A[0, :] = A[1, :]
A[2, :] = A[1, :]
(U, S, V) = torch.pca_lowrank(A, q=None, center=True, niter=2)