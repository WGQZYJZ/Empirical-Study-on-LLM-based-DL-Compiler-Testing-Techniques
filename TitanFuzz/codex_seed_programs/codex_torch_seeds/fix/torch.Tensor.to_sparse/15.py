'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.to_sparse(sparseDims=2)
print('Output tensor: {}'.format(_output_tensor))