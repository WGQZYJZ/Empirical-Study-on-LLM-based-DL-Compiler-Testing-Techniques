'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bfloat16\ntorch.Tensor.bfloat16(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(1, 2, 3, 4)
_output_tensor = torch.Tensor.bfloat16(_input_tensor, memory_format=torch.preserve_format)
print('_output_tensor = ', _output_tensor)