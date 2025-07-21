'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(low=0, high=2, size=(3, 3, 3), dtype=torch.int32)
print('Input Tensor: ', _input_tensor)
_bool_tensor = _input_tensor.bool()
print('Boolean Tensor: ', _bool_tensor)