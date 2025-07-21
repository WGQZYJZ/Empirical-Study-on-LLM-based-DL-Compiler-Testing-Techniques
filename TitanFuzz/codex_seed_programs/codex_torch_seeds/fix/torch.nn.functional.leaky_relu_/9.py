'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
import torch
input_data = torch.randn(10)
print(input_data)
print(torch.nn.functional.leaky_relu_(input_data))
print(torch.nn.functional.leaky_relu_(input_data, negative_slope=0.1))
print(torch.nn.functional.leaky_relu_(input_data, negative_slope=0.2))