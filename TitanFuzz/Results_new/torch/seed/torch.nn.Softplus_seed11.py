data = np.random.randn(10, 10)
tensor = torch.tensor(data)
softplus = torch.nn.Softplus(beta=1, threshold=20)
output = softplus(tensor)