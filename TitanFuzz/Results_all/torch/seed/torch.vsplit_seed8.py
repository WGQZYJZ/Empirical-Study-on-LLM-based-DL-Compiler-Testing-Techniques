x = torch.arange(16, dtype=torch.float32).view(4, 4)
torch.vsplit(x, 2)
x = torch.arange(16, dtype=torch.float32).view(4, 4)
torch.chunk(x, 2, dim=0)
x = torch.arange(16, dtype=torch.float32).view(4, 4)
torch