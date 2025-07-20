x = torch.rand(2, 3)
y = torch.nn.functional.leaky_relu_(x, negative_slope=0.01)