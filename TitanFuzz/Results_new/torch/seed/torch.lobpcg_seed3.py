A = np.random.rand(100, 100)
A = torch.from_numpy(A)
torch.lobpcg(A)