input = torch.randn(5, 2, 3)
output = torch.cumprod(input, dim=1)