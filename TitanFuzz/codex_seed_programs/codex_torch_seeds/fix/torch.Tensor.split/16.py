'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.split\ntorch.Tensor.split(_input_tensor, split_size, dim=0)\n'
import torch
input_tensor = torch.randn(10, 4)
print('Input Tensor: ', input_tensor)
output_tensor_list = input_tensor.split(split_size=2, dim=0)
print('Output Tensor List: ', output_tensor_list)
print('Output Tensor 1: ', output_tensor_list[0])
print('Output Tensor 2: ', output_tensor_list[1])
print('Output Tensor 3: ', output_tensor_list[2])
print('Output Tensor 4: ', output_tensor_list[3])
print('Output Tensor 5: ', output_tensor_list[4])