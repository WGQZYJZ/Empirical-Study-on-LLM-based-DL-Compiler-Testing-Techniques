'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
input_data = torch.tensor([[(- 1.0), (- 0.5), 0.0, 0.5, 1.0]])
tanh = torch.nn.Tanh()
output_data = tanh(input_data)
print(output_data)