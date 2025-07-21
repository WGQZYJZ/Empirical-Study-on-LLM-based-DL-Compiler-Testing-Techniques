'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hsplit\ntorch.Tensor.hsplit(_input_tensor, split_size_or_sections)\n'
import torch
import torch
input_tensor = torch.arange(start=0, end=12, step=1, dtype=torch.float32).reshape(3, 4)
output_tensor_list = input_tensor.hsplit(split_size_or_sections=2)
print('The input tensor is: ', input_tensor)
print('The output tensor list is: ', output_tensor_list)