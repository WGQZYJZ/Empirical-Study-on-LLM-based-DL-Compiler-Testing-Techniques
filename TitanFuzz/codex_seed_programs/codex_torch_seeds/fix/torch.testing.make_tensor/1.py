'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.testing.make_tensor\ntorch.testing.make_tensor(shape, device, dtype, *, low=None, high=None, requires_grad=False, noncontiguous=False, exclude_zero=False)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]])
print('Input data: ', input_data)
output_data = torch.testing.make_tensor(input_data.shape, device=torch.device('cpu'), dtype=torch.float32)
print('Output data: ', output_data)