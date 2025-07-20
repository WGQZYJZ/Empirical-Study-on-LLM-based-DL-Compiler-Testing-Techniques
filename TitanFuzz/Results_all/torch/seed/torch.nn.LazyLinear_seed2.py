x = torch.randn(10, 3)
lazy_linear = torch.nn.LazyLinear(3, 4)
y = lazy_linear(x)
weight = lazy_linear.weight
bias = lazy_linear.bias