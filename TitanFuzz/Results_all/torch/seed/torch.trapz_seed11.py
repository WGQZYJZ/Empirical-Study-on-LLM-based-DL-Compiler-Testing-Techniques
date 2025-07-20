x = torch.arange(0, 3, 0.1)
y = torch.sin(x)
result = torch.trapz(y, dx=0.1)