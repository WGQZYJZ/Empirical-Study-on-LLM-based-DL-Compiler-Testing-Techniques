'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
import numpy as np
input_data = torch.tensor([[(- 1.0), (- 2.0), (- 3.0)], [1.0, 2.0, 3.0]])
print(input_data)
tanh_output = torch.nn.Tanh()
output = tanh_output.forward(input_data)
print(output)