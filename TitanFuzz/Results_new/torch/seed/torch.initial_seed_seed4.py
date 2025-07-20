x = torch.rand(10000, 1)
y = torch.rand(10000, 1)
torch.initial_seed()
z = (x + y)