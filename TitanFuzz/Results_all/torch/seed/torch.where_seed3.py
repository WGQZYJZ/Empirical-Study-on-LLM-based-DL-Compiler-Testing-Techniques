condition = torch.tensor([True, False])
x = torch.tensor([1, 2])
y = torch.tensor([3, 4])
out = torch.where(condition, x, y)