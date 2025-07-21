'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
input_data = torch.tensor([(- 1.0), 1.0, 2.0, 3.0])
output_data = torch.nn.Tanh()(input_data)
print(output_data)