'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sqrt\ntorch.Tensor.sqrt(_input_tensor)\n'
import torch
input_tensor = torch.arange(1, 11)
output_tensor = input_tensor.sqrt()
print('input_tensor =', input_tensor)
print('output_tensor =', output_tensor)