input = torch.randn(7, 4)
output = torch.tensor_split(input, 3, dim=0)