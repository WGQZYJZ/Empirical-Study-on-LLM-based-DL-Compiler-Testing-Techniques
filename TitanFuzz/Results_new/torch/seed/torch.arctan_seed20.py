a = torch.randn(1, requires_grad=True)
result = torch.arctan(a)
result.backward()