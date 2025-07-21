'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
x = torch.randn(1, 3)
print('Input:', x)
y = x.round()
print('Output:', y)