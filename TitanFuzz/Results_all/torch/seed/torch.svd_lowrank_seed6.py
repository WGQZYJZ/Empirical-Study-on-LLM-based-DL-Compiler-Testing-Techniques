A = torch.randn(10, 10)
q = 6
niter = 2
M = None
(U, S, V) = torch.svd_lowrank(A, q=q, niter=niter, M=M)