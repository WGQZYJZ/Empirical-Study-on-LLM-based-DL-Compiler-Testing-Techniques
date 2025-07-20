x = torch.rand(5, 3, requires_grad=True)
with torch.no_grad():
    y = (x * 2)
    print(y)