x = torch.ones(2, 2, requires_grad=True)
with torch.no_grad():
    y = (x + 2)
    print(y)