A = torch.tensor(np.random.rand(10, 20))
result = torch.pca_lowrank(A, q=None, center=True, niter=2)