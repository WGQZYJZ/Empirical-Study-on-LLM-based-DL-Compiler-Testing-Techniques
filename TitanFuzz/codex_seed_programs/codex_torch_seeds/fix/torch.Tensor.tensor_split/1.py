'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3))
print('Input data: \n', input_tensor)
output_tensor = torch.Tensor.tensor_split(input_tensor, 3, dim=0)
print('Output data: \n', output_tensor)