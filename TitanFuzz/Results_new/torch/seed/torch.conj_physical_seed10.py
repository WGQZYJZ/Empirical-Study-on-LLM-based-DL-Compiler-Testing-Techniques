input = torch.randn(3, 4, dtype=torch.float32, requires_grad=True)
output = torch.conj_physical(input)