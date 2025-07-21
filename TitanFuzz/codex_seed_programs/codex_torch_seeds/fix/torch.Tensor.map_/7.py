'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.map_\ntorch.Tensor.map_(_input_tensor, tensor, callable\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.map_(input_tensor, (lambda x: (x * x)))
print(output_tensor)