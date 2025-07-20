x = torch.tensor([True, True, False, False], dtype=torch.bool)
y = torch.tensor([True, False, True, False], dtype=torch.bool)
z = torch.logical_xor(x, y)