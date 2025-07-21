'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
source = torch.tensor([0.0, (- 1.0)])
output_tensor = torch.Tensor.put_(input_tensor, index, source, accumulate=False)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)