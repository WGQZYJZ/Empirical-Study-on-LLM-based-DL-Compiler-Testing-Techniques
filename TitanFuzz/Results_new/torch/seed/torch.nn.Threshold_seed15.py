data = np.random.randn(1, 2, 3, 3)
data = torch.Tensor(data)
out = torch.nn.Threshold(0.5, 0.0)(data)