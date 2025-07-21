'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp\ntorch.Tensor.lerp(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.randn(3, 3)
end = torch.randn(3, 3)
weight = torch.randn(1)
output_tensor = torch.Tensor.lerp(input_tensor, end, weight)
print('Input Tensor:')
print(input_tensor)
print('End Tensor:')
print(end)
print('Weight:')
print(weight)
print('Output Tensor:')
print(output_tensor)