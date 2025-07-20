x = torch.randn(3, requires_grad=True)
y = torch.randn(3, requires_grad=True)
z = torch.dist(x, y, p=2)
z.backward()