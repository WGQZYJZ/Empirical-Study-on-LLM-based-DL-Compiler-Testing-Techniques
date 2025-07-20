x = torch.rand(1, requires_grad=True)
y = (x * 2)
z = y.mean()
graph = torch.fx.Graph(z)