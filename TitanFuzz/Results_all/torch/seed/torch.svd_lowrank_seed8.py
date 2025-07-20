A = torch.randn(8, 8)
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)