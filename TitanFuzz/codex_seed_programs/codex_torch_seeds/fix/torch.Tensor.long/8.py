'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randint(0, 10, (3, 4))
_input_tensor_long = _input_tensor.long()
print(_input_tensor_long)