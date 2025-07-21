'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.minimum\ntorch.Tensor.minimum(_input_tensor, other)\n'
import torch
import torch
input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
output_tensor = torch.Tensor.minimum(input_tensor, other)
print(output_tensor)