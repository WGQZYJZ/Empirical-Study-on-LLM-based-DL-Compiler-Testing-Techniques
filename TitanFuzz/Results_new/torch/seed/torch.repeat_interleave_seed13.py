input = torch.tensor([[1, 2], [3, 4]])
output = torch.repeat_interleave(input, repeats=2, dim=0)