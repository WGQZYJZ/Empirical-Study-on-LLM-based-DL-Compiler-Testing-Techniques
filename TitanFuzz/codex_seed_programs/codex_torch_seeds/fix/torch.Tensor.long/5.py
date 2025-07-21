'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = _input_tensor.long()
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)