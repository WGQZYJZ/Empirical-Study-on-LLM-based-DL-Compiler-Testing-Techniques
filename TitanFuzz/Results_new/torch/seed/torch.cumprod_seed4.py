input = torch.randn(2, 3)
output = torch.cumprod(input, dim=1)