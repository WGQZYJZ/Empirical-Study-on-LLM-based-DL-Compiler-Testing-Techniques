'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4, 5)
output_tensor = input_tensor.to_mkldnn()
print('input tensor:', input_tensor)
print('output tensor:', output_tensor)