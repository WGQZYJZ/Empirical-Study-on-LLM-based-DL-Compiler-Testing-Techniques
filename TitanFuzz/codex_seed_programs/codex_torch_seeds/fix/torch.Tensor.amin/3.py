'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.amin\ntorch.Tensor.amin(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.rand(2, 3)
print('Input Tensor: \n', input_tensor)
amin_result = torch.Tensor.amin(input_tensor, dim=1, keepdim=False)
print('Output Tensor: \n', amin_result)