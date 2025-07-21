'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
import torch
input_data = torch.randn(1, 3, 3, 3)
print(input_data)
output_data = torch.nn.functional.leaky_relu_(input_data)
print(output_data)