'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isreal\ntorch.Tensor.isreal(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 4, dtype=torch.float32)
is_real = _input_tensor.isreal()
print('The input tensor is real: ', is_real)