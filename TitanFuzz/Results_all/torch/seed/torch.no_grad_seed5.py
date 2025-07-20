x = torch.rand(5, 3)
y = torch.rand(5, 3)
with torch.no_grad():
    z = (x + y)
    print(z)