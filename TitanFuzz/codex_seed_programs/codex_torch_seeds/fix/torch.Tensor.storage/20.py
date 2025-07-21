'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage\ntorch.Tensor.storage(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
print('storage of input_tensor: ', input_tensor.storage())