'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
sum_to_size_output = torch.Tensor.sum_to_size(_input_tensor, 2, 3, 4, 5)
print(sum_to_size_output)