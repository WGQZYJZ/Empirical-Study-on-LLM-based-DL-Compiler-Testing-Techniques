x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([6, 7, 8, 9, 10])
condition = (x > 3)
z = torch.where(condition, x, y)