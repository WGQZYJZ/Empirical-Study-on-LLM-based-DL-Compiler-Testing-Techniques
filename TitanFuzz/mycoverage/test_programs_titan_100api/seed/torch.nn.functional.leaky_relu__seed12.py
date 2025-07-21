x = torch.randn(1, 1, 5, 5)
y = torch.nn.functional.leaky_relu_(x, negative_slope=0.01)