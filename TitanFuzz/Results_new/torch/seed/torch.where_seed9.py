cond = torch.tensor([True, False, False, True], dtype=torch.bool)
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([9, 8, 7, 6])
out = torch.where(cond, x, y)