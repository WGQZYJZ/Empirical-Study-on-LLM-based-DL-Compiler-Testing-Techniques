x = torch.empty(5, 3)
y = torch.randn_like(x, dtype=torch.float)
y = torch.randn(5, 3, dtype=torch.float)
y = torch.randn_like(x, dtype=torch.double)
y = torch.randn(5, 3, dtype=torch.double)
y = torch.randn_like(x, dtype=torch.half)
y = torch.randn