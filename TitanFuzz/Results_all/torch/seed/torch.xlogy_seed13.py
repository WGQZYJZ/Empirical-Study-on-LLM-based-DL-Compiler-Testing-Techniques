input = torch.randn(4, 4)
other = torch.randn(4, 4)
xlogy = torch.xlogy(input, other)
xlogy_ = torch.xlogy_(input, other)