a = torch.randn(2, 3, 4)
b = torch.randn(2, 1, 4)
c = torch.broadcast_shapes(a.shape, b.shape)