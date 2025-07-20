x = torch.randn(2, 3, requires_grad=True)
linear = torch.nn.LazyLinear(3, 2)
y = linear(x)