'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
import torch
input_tensor = torch.randn(4, 4, 4)
print(input_tensor)
output_tensor_list = torch.Tensor.dsplit(input_tensor, 2)
print(output_tensor_list)