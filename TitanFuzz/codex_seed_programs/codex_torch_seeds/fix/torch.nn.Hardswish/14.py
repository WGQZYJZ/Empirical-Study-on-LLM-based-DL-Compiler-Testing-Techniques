'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
input_data = torch.randn(10, 20, 30, 40)
hardswish = torch.nn.Hardswish()
output = hardswish(input_data)
print(output)