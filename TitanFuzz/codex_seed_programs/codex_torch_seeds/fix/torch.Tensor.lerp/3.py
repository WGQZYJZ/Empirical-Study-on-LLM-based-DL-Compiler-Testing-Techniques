'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lerp\ntorch.Tensor.lerp(_input_tensor, end, weight)\n'
import torch
input_tensor = torch.rand(4, 4)
end = torch.rand(4, 4)
weight = 0.5
output_tensor = torch.Tensor.lerp(input_tensor, end, weight)
print('The input tensor is:')
print(input_tensor)
print('The end tensor is:')
print(end)
print('The output tensor is:')
print(output_tensor)