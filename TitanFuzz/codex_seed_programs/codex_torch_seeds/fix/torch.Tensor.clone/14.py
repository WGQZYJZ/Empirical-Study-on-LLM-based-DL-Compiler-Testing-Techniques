'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clone\ntorch.Tensor.clone(_input_tensor, *, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.rand(4, 4)
print('The input tensor:')
print(input_tensor)
output_tensor = input_tensor.clone()
print('The output tensor:')
print(output_tensor)