x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
y = torch.tensor([[10, 20], [30, 40]], dtype=torch.float32)
out = torch.lerp(x, y, 0.5)