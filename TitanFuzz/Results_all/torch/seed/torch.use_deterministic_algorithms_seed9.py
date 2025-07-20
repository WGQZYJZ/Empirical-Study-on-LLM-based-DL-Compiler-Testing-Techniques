x = torch.randn(4, 4)
y = torch.randn(4, 4)
torch.use_deterministic_algorithms(mode=True)
z = (x + y)