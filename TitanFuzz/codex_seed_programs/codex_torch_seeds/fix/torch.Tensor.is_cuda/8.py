'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_cuda\ntorch.Tensor.is_cuda(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
_output_tensor = torch.Tensor.is_cuda(_input_tensor)
print('The input tensor: {}'.format(_input_tensor))
print('The output tensor: {}'.format(_output_tensor))