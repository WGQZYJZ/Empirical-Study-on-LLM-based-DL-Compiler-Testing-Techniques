'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.to_sparse(sparseDims=1)
print('input tensor: ', _input_tensor)
print('output tensor: ', _output_tensor)