input = torch.randn(2, 3)
repeats = 2
dim = 0
output = torch.repeat_interleave(input, repeats, dim)