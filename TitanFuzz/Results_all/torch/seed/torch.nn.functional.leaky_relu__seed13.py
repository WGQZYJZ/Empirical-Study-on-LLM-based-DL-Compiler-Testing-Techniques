input = torch.randn(1, 1, 3, 3)
output = torch.nn.functional.leaky_relu_(input)