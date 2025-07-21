'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.initial_seed\ntorch.initial_seed()\n'
import torch
input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
torch.initial_seed()
print('Input data: ', input_data)
print('Output data: ', torch.initial_seed())