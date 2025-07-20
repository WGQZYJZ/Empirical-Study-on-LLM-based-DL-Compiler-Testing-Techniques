input = torch.randn(3, 4)
output = torch.transpose(input, 0, 1)
output = torch.t(input)