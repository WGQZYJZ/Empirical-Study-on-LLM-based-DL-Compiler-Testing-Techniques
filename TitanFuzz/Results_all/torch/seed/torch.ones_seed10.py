x = torch.ones(2, 2, requires_grad=True)
y = (x + 2)
z = ((y * y) * 3)
out = z.mean()
a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
a.requires_grad_(True)
b = (a * a).sum()
out.backward()
x = torch.randn(3, requires_grad=True)
y = (x * 2)
while (y.data.norm() < 1000):
    y = (y * 2)
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)