'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage\ntorch.Tensor.storage(_input_tensor)\n'
import torch
_input_tensor = torch.rand(size=(10,))
print(torch.Tensor.storage(_input_tensor))