'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.contiguous\ntorch.Tensor.contiguous(_input_tensor, memory_format=torch.contiguous_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 5)
print(_input_tensor)
print(_input_tensor.contiguous())
print(_input_tensor.contiguous(memory_format=torch.channels_last))
'\nTask 4: Call the API torch.Tensor.detach\ntorch.Tensor.detach()\n'
_input_tensor = torch.randn(2, 3, 5)
print(_input_tensor)
print(_input_tensor.detach())
'\nTask 5: Call the API torch.Tensor.detach_\ntorch.Tensor.detach_()\n'
_input_tensor = torch.randn(2, 3, 5)
print(_input_tensor)
print(_input_tensor.detach_())
'\nTask 6: Call the API torch.Tensor.dim\ntorch.Tensor.dim()\n'
_input_tensor = torch.randn(2, 3, 5)
print(_input_tensor)