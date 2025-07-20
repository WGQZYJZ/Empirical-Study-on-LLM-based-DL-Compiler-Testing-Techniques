x = torch.tensor([[1, 2, 3], [4, 5, 6]])
y = torch.tensor([[7, 8, 9], [10, 11, 12]])
torch.set_warn_always(True)
z = torch.add(x, y)