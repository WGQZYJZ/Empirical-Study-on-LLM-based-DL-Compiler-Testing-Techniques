'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
input_data = torch.randn(1, 1, 3, 5)
relu6 = torch.nn.ReLU6()
output = relu6(input_data)
print(input_data)
print(output)