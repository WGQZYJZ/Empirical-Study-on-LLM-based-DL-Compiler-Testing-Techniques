A = torch.randn(10, 10)
(u, s, v) = torch.svd_lowrank(A, q=6, niter=2, M=None)