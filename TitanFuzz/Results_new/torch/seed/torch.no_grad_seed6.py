x = torch.randn(3, requires_grad=True)
with torch.no_grad():
    y = (x * 2)
    print('y = ', y)
z = y.detach()