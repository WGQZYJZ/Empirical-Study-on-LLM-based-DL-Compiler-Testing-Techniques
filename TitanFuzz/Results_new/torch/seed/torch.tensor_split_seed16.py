input = torch.randn(2, 3, 4)
output = torch.tensor_split(input, 2, dim=0)
output = torch.tensor_split(input, 3, dim=1)
output = torch.tensor_split(input, 4, dim=2)