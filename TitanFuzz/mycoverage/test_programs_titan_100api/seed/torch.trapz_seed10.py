x = torch.arange(1, 5, 0.1)
y = torch.sin(x)
z = torch.trapz(y, dx=0.1, dim=0)