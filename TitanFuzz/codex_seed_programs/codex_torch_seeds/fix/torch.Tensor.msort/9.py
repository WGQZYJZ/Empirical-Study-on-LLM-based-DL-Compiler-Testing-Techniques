'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print('input tensor: ', input_tensor)
sorted_tensor = input_tensor.msort(dim=0)
print('sorted tensor: ', sorted_tensor)