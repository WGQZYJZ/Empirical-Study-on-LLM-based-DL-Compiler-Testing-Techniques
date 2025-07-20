x = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
y = torch.tensor([1, 2, 3, 4, 5], dtype=torch.float32)
condition = (x > y)
z = torch.where(condition, x, y)