input = torch.rand(3, 4)
output = torch.cumprod(input, dim=1)