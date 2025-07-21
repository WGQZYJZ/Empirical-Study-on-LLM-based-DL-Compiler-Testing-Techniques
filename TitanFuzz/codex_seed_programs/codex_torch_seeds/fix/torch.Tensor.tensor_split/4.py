'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
import torch
input_tensor = torch.arange(1, 9, dtype=torch.float32).reshape(2, 4)
print('Input tensor: \n', input_tensor)
output_tensor_list = torch.Tensor.tensor_split(input_tensor, 2, dim=1)
print('Output tensor list: \n', output_tensor_list)