'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.get_device\ntorch.Tensor.get_device(_input_tensor)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.randn(2, 3, 4)
print('Task 3: Call the API torch.Tensor.get_device')
device = input_tensor.get_device()
print(device)