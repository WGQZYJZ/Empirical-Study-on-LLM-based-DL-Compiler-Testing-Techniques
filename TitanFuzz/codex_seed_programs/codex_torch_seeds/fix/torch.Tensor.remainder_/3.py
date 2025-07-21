'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randint(low=1, high=10, size=(5,), dtype=torch.float)
print('input_tensor = \n', input_tensor)
divisor = torch.tensor(3.14)
output_tensor = input_tensor.remainder_(divisor)
print('output_tensor = \n', output_tensor)