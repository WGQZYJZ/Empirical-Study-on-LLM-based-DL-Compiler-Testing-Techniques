x = torch.randn(2, 3, 4)
y = torch.tensor_split(x, 3, dim=2)