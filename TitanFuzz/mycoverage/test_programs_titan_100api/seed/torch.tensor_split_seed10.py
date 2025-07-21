input = torch.rand(5, 3, 10)
output = torch.tensor_split(input, 5, dim=0)