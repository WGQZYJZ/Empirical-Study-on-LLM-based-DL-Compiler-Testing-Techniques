'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
input_tensor = torch.arange(18, dtype=torch.float32).reshape(6, 3)
print('The input tensor is:\n{}'.format(input_tensor))
split_size = 2
output_tensor_list = input_tensor.vsplit(split_size)
print('The output tensor list is:')
for (i, tensor) in enumerate(output_tensor_list):
    print('{}: \n{}'.format(i, tensor))
split_size = [2, 3]
output_tensor_list = input_tensor.vsplit(split_size)
print('The output tensor list is:')
for (i, tensor) in enumerate(output_tensor_list):
    print('{}: \n{}'.format(i, tensor))