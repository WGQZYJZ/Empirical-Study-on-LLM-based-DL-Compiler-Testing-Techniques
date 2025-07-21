'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder\ntorch.Tensor.remainder(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randn(3, 3)
divisor = torch.tensor([2, 3, 4])
output_tensor = input_tensor.remainder(divisor)
print('input_tensor is: \n', input_tensor)
print('divisor is: \n', divisor)
print('output_tensor is: \n', output_tensor)