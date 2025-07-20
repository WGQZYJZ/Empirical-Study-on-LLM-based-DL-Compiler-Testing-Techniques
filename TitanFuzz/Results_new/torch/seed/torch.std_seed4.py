input = torch.randn(3, 3)
std = torch.std(input, dim=1)
std = torch.std(input, dim=1, unbiased=False)