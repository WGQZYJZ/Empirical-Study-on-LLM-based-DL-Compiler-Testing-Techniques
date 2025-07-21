'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
input_data = torch.ones(2, 2)
torch.nn.init.ones_(input_data)
print(input_data)