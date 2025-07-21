'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arctan\ntorch.Tensor.arctan(_input_tensor)\n'
import torch
input_tensor = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
output_tensor = torch.Tensor.arctan(input_tensor)
print('Input: ', input_tensor)
print('Output: ', output_tensor)
'\nTask 4: Call the API torch.arctan\ntorch.arctan(_input_tensor)\n'
import torch
input_tensor = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
output_tensor = torch.arctan(input_tensor)
print('Input: ', input_tensor)
print('Output: ', output_tensor)