x = torch.tensor([(- 1), 0, 1], dtype=torch.float)
softplus = torch.nn.Softplus(beta=1, threshold=20)
y = softplus(x)