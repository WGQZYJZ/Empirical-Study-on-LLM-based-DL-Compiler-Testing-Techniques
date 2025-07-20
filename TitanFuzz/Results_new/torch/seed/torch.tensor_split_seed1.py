input = torch.arange(start=1, end=25, dtype=torch.float32).reshape(4, 6)
output = torch.tensor_split(input, 3, dim=0)