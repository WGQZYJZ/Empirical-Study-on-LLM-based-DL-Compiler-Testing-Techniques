'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
import torch
input_tensor = torch.arange(start=0, end=12, dtype=torch.float32)
input_tensor = input_tensor.view(1, 1, 12)
print('Input tensor: {}'.format(input_tensor))
output_tensor = torch.Tensor.tensor_split(input_tensor, [3, 6, 9], dim=2)
print('Output tensor: {}'.format(output_tensor))