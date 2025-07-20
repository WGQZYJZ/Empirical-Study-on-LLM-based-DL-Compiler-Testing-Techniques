input = torch.tensor([[1, 2, 3], [4, 5, 6]])
repeats = torch.tensor([2, 3])
output = torch.repeat_interleave(input, repeats, dim=0)