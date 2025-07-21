'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log1p_\ntorch.Tensor.log1p_(_input_tensor)\n'
import torch
input_tensor = torch.randint(10, (2, 3), dtype=torch.float)
torch.Tensor.log1p_(input_tensor)
print('The result of torch.Tensor.log1p_ is: ', input_tensor)