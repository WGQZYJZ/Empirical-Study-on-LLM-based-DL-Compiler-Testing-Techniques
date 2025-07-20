input = torch.randn(4, 4)
index = torch.tensor([0, 2])
output = torch.take(input, index)