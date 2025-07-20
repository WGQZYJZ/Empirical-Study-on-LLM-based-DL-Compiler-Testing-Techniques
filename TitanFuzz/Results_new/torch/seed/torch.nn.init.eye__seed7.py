x = torch.empty(3, 3)
y = torch.empty(3, 3)
torch.nn.init.eye_(x)
torch.nn.init.eye_(y)