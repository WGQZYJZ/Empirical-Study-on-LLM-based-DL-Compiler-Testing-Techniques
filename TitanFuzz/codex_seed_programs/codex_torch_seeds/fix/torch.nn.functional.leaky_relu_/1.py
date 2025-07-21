'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.leaky_relu_\ntorch.nn.functional.leaky_relu_(input, negative_slope=0.01)\n'
import torch
import numpy as np
input_data = torch.tensor(np.random.rand(10, 10), dtype=torch.float)
print(input_data)
print(torch.nn.functional.leaky_relu_(input_data))
output_data = torch.nn.functional.leaky_relu_(input_data)
print(output_data)