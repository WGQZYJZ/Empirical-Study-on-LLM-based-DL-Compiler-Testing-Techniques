'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.argmax\ntorch.Tensor.argmax(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor = torch.randn(1, 3)
print('input_tensor =', input_tensor)
print('max_index =', input_tensor.argmax())
print('max_index =', input_tensor.argmax(0))
print('max_index =', input_tensor.argmax(1))
print('max_index =', input_tensor.argmax(dim=0))
print('max_index =', input_tensor.argmax(dim=1))
print('max_index =', input_tensor.argmax(keepdim=True))
print('max_index =', input_tensor.argmax(dim=0, keepdim=True))
print('max_index =', input_tensor.argmax(dim=1, keepdim=True))