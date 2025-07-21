'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
output_tensor = input_tensor.sign()
print('Input tensor:\n', input_tensor)
print('Output tensor:\n', output_tensor)