input = torch.randn(2, 3, 4)
output = torch.repeat_interleave(input, 3, dim=1)