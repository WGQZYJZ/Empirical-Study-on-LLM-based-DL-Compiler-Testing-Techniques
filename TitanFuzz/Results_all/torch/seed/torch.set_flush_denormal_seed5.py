x = torch.randn(1, 1, 3, 3, dtype=torch.float32)
y = torch.randn(1, 1, 3, 3, dtype=torch.float32)
torch.set_flush_denormal(True)
z = (x + y)