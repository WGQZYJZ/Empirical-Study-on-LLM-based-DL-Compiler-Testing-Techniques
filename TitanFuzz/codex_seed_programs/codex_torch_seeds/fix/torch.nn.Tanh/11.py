'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
input_data = torch.randn(1, 5)
tanh_out = torch.nn.Tanh()(input_data)
print(tanh_out)