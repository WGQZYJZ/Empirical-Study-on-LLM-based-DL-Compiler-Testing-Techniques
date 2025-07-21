'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224, requires_grad=True)
output_tensor = input_tensor.detach()
print('Output tensor: {}'.format(output_tensor))