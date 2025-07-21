'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.short\ntorch.Tensor.short(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4, 5, dtype=torch.float32)
_out_tensor = _input_tensor.short()
print('The input tensor is: ', _input_tensor)
print('The output tensor is: ', _out_tensor)