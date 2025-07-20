input = torch.arange(2)
repeats = torch.tensor([3, 2])
output = torch.repeat_interleave(input, repeats, dim=0)