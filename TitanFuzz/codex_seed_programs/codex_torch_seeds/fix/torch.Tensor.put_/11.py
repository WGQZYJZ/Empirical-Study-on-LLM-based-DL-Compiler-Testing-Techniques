'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('input_tensor: ', input_tensor)
index = [1, 0]
source = torch.tensor([1, 2])
input_tensor.put_(index, source)
print('input_tensor after put_: ', input_tensor)