'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: \n', input_tensor)
indices = torch.tensor([[0, 0], [1, 1], [2, 2]], dtype=torch.long)
values = torch.tensor([0.5, 1.5, 2.5], dtype=torch.float)
input_tensor.index_put((indices, values), accumulate=False)
print('Output Tensor: \n', input_tensor)