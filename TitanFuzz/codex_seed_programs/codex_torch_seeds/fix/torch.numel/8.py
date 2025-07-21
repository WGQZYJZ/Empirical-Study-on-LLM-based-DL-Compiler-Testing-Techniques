'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.numel\ntorch.numel(input)\n'
import torch
x = torch.rand(2, 3, 4)
num_elements = torch.numel(x)
print('Num elements: ', num_elements)