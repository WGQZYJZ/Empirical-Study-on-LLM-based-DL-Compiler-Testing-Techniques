x = torch.rand(2, 3)
y = torch.rand(2, 3)
torch.set_warn_always(True)
z = torch.add(x, y)