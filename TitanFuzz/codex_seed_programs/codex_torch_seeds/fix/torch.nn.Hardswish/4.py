'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
input_data = torch.randn(1, 3, 224, 224)
hardswish = torch.nn.Hardswish(inplace=False)
output = hardswish(input_data)
print(output)