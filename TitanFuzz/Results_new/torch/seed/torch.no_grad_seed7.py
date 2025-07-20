x = torch.randn(5, 5, requires_grad=True)
with torch.no_grad():
    y = (x * 2)
    print(y)