x = torch.randn(1, 1, requires_grad=True, dtype=torch.float32)
y = torch.randn(1, 1, requires_grad=True, dtype=torch.float32)
z = (x * y)
torch.are_deterministic_algorithms_enabled()