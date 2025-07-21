import torch
x = torch.randn(3, 3)
y = torch.nn.functional.leaky_relu(x, negative_slope=0.01, inplace=False)