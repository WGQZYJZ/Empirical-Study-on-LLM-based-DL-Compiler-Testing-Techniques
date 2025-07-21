'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.signbit\ntorch.Tensor.signbit(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.signbit(input_tensor)
print('The input_tensor is: ', input_tensor)
print('The output_tensor is: ', output_tensor)