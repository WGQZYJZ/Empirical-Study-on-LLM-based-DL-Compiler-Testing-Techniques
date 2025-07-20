x = torch.tensor([2.0, 3.0], requires_grad=True)
with torch.enable_grad():
    y = (x ** 2)
    z = y.mean()
z.backward()