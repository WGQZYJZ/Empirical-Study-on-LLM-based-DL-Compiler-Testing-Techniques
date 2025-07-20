a = torch.rand(2, 2)
b = torch.rand(2, 2)
torch.use_deterministic_algorithms(mode=True)
c = (a + b)