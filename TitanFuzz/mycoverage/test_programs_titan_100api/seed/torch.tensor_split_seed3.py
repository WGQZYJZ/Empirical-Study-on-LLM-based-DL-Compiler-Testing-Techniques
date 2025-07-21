input = torch.randn(3, 5)
result = torch.tensor_split(input, 2, dim=1)