'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
import torch
input_tensor = torch.arange(0, 12).view(3, 4)
print('input:')
print(input_tensor)
indices = torch.tensor([0, 2])
output_tensor = input_tensor.take(indices)
print('output:')
print(output_tensor)