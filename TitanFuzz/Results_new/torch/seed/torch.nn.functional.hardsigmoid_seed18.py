x = torch.tensor(np.random.randn(1, 3, 3), dtype=torch.float)
y = torch.nn.functional.hardsigmoid(x)