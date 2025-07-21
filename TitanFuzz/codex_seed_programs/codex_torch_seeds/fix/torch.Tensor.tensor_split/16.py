'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.arange(start=0, end=12, step=1, dtype=torch.float32)
print('Input Tensor:')
print(input_tensor)
print('Task 3: Call the API torch.Tensor.tensor_split')
output_tensor_list = input_tensor.tensor_split(indices_or_sections=(3, 3, 3), dim=0)
print('Output Tensor List:')
for output_tensor in output_tensor_list:
    print(output_tensor)