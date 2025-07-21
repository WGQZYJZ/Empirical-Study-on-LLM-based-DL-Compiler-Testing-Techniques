'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
import torch
input_data = torch.randn(1, 3, 224, 224)
output = torch.nn.functional.hardswish(input_data)
print('output size: ', output.size())