x = torch.randn(2, 3)
y = torch.nn.Softmin(dim=1)(x)