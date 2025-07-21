'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.randn(4, 4)
print('input_tensor: ', input_tensor)
index = torch.tensor([0, 2])
source = torch.tensor([100, 200])
input_tensor.put_(index, source, accumulate=False)
print('output_tensor: ', input_tensor)