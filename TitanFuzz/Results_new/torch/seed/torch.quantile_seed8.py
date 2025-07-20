input = torch.randn(2, 3)
quantile = torch.quantile(input, 0.5, dim=1, keepdim=True)