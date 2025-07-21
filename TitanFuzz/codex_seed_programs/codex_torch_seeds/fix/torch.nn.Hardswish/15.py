'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
input_data = torch.randn(2, 3, 4, 5)
relu6 = torch.nn.Hardswish(inplace=False)
print(relu6(input_data))