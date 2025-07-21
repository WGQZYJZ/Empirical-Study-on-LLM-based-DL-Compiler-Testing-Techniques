'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
_input_tensor = torch.tensor([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0]])
print('_input_tensor = \n', _input_tensor)
_sparse_tensor_1 = _input_tensor.to_sparse(0)
print('_sparse_tensor_1 = \n', _sparse_tensor_1)
_sparse_tensor_2 = _input_tensor.to_sparse(1)