'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.byte\ntorch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(3, 3, 3)
_output_tensor = torch.Tensor.byte(_input_tensor, memory_format=torch.preserve_format)
print('input tensor: ', _input_tensor)
print('output tensor: ', _output_tensor)