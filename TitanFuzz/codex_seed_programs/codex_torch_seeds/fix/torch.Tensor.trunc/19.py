'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 224, 224)
output_tensor = input_tensor.trunc()
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)