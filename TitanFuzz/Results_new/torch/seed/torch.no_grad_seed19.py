x = torch.rand(1, requires_grad=True)
with torch.no_grad():
    y = (x * 2)
    print(y)
with torch.no_grad():
    y = (x.detach() * 2)
    print(y)