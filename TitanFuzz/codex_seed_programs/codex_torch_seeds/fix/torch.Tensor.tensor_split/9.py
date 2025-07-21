'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
input_tensor = torch.arange(start=1, end=13, dtype=torch.float32).reshape(3, 4)
print('Input tensor: \n{}'.format(input_tensor))
output_tensors = torch.Tensor.tensor_split(input_tensor, 2, dim=1)
print('Output tensors: \n{}'.format(output_tensors))