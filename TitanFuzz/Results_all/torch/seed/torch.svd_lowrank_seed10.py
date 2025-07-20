A = torch.randn(10, 10)
(U, S, V) = torch.svd_lowrank(A, q=6, niter=2, M=None)
(U, S, V) = torch.svd(A, some=False, compute_uv=True, out=None)