'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.get_device\ntorch.Tensor.get_device(_input_tensor)\n'
import torch
input_data = torch.randn(5, 3)
print('Input Data:', input_data)
device = torch.Tensor.get_device(input_data)
print('Device:', device)