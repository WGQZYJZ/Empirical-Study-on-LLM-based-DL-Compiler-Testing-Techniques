x = torch.randn(4)
y = torch.randn(4)
z = torch.empty(4)
torch.lerp(x, y, 0.5, out=z)