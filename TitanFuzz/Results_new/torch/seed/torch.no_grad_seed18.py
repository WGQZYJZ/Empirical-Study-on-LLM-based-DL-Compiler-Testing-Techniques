x = torch.randn(3, requires_grad=True)
y = (x * 2)
with torch.no_grad():
    y = (x * 2)
    print(y)