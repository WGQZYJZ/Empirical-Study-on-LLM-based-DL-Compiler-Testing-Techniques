input = torch.randn(2, 3)
repeats = torch.tensor([1, 2])
output = torch.repeat_interleave(input, repeats, dim=0)