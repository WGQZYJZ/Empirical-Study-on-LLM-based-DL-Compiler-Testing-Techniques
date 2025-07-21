'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not\ntorch.Tensor.bitwise_not(_input_tensor)\n'
import torch
input_tensor = torch.randint(0, 2, (3, 3), dtype=torch.uint8)
print('input_tensor = \n', input_tensor)
output_tensor = torch.Tensor.bitwise_not(input_tensor)
print('output_tensor = \n', output_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ceil\ntorch.Tensor.ceil(_input_tensor)\n'
import torch
input_tensor = torch.rand((3, 3))
print('input_tensor = \n', input_tensor)
output_tensor = torch.Tensor.ceil(input_tensor)