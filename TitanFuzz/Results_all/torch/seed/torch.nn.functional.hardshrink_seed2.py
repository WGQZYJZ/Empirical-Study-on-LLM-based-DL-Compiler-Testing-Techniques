data = torch.randn(3, 3)
output = torch.nn.functional.hardshrink(data, lambd=0.5)