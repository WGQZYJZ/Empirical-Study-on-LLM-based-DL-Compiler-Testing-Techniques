'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(f'input_tensor: {input_tensor}')
output_tensor = input_tensor.rad2deg()
print(f'output_tensor: {output_tensor}')