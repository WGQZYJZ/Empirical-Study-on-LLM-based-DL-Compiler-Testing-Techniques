x = torch.rand(10, dtype=torch.float32)
torch.use_deterministic_algorithms(mode=True)
y = torch.rand(10, dtype=torch.float32)