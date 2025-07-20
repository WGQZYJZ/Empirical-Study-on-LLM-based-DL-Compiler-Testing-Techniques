x = torch.randn(1, requires_grad=True)
with torch.no_grad():
    y = (x * 2)