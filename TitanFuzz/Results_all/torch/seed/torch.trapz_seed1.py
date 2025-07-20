x = torch.linspace(0, (2 * np.pi), steps=100, dtype=torch.float64)
y = torch.sin(x)
integral = torch.trapz(y, x=x)
integral = torch.trapz(y, x=x)