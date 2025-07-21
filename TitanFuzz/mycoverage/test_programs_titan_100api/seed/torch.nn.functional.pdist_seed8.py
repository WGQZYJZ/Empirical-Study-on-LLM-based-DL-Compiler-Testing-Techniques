x = torch.randn(2, 3)
y = torch.nn.functional.pdist(x, p=2)