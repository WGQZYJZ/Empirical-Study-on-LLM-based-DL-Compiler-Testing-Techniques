'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = input_tensor.unsqueeze(0)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)