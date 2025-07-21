'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
import torch
input_tensor = torch.arange(0, 12)
index = torch.tensor([0, 2, 4, 6, 8, 10])
source = torch.tensor([100, 200, 300, 400, 500, 600])
input_tensor.put_(index, source, accumulate=False)
print('input_tensor: ', input_tensor)