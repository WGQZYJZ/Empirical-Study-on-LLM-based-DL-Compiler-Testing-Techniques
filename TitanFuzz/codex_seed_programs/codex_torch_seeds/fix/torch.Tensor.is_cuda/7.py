'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_cuda\ntorch.Tensor.is_cuda(_input_tensor, )\n'
import torch
_input_tensor = torch.rand(3, 4)
is_cuda = torch.Tensor.is_cuda(_input_tensor)
print(is_cuda)
'\nTask 4: Call the API torch.Tensor.is_floating_point\ntorch.Tensor.is_floating_point(_input_tensor, )\n'
is_floating_point = torch.Tensor.is_floating_point(_input_tensor)
print(is_floating_point)
'\nTask 5: Call the API torch.Tensor.is_complex\ntorch.Tensor.is_complex(_input_tensor, )\n'
is_complex = torch.Tensor.is_complex(_input_tensor)
print(is_complex)
'\nTask 6: Call the API torch.Tensor.is_sparse\ntorch.Tensor.is_sparse(_input_tensor, )\n'