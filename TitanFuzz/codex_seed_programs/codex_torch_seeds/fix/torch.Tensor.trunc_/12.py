'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc_\ntorch.Tensor.trunc_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1.5, 2.5, 3.5], [(- 1.5), (- 2.5), (- 3.5)]])
output_tensor = torch.Tensor.trunc_(input_tensor)
print('The input tensor: ', input_tensor)
print('The output tensor: ', output_tensor)