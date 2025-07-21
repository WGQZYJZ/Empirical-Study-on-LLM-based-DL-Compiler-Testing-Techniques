'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acos_\ntorch.Tensor.acos_(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([1, (- 1), 0.5])
torch.Tensor.acos_(input_tensor)
print('The result of the acos_ API: {}'.format(input_tensor))