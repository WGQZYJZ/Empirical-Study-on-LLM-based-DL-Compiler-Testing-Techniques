input = torch.randn(2, 3, 4)
torch.nn.functional.glu(input, dim=(- 1))
input = torch.randn(2, 3, 4)
torch.nn.functional.hardshrink(input, lambd=0.5)