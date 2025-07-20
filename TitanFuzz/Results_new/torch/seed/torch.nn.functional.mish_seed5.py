x = torch.randn(2, 3, requires_grad=True)
y = torch.nn.functional.mish(x)