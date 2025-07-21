'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_not_\ntorch.Tensor.logical_not_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[True, False, False], [False, True, False], [False, False, True]], dtype=torch.bool)
print('Input Tensor:\n', input_tensor)
output_tensor = torch.Tensor.logical_not_(input_tensor)
print('Output Tensor:\n', output_tensor)