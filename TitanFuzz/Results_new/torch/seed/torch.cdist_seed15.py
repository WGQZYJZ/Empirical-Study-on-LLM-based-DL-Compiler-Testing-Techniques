x1 = torch.randn(100, 128)
x2 = torch.randn(200, 128)
dist = torch.cdist(x1, x2, p=2.0)