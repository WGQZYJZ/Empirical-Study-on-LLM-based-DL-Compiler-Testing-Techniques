'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.arange(start=0, end=12, step=1, dtype=torch.float32)
input_tensor = input_tensor.reshape(3, 4)
print('input_tensor = \n{0}'.format(input_tensor))
print('Task 3: Call the API torch.Tensor.tensor_split')
indices_or_sections = [1, 2]
output_tensor_list = torch.Tensor.tensor_split(input_tensor, indices_or_sections, dim=0)
print('indices_or_sections = {0}'.format(indices_or_sections))
print('output_tensor_list = \n{0}'.format(output_tensor_list))
indices_or_sections = [2, 1]
output_tensor_list = torch.Tensor.tensor_split