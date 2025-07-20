x = torch.randn(1, 2, 3, 4)
y = torch.randn(5, 6)
graph = torch.fx.Graph(x, y)