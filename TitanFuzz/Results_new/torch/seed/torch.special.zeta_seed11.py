input = torch.tensor([2, 3, 4, 5], dtype=torch.float32)
other = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
output = torch.special.zeta(input, other)