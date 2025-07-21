'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze_\ntorch.Tensor.unsqueeze_(_input_tensor, dim)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input Tensor:')
print(input_tensor)
output_tensor = input_tensor.unsqueeze_(dim=0)
print('Output Tensor:')
print(output_tensor)