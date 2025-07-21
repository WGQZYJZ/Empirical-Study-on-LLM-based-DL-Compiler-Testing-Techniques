'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater\ntorch.Tensor.greater(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output_tensor = torch.Tensor.greater(input_tensor, 3)
print('input_tensor = ', input_tensor)
print('output_tensor = ', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.max\ntorch.Tensor.max(_input_tensor, dim=None, keepdim=False, out=None)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)