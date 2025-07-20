x = torch.randn(4, 6)
y = torch.tensor_split(x, 3, dim=1)
z = torch.tensor_split(x, [1, 2, 3], dim=1)