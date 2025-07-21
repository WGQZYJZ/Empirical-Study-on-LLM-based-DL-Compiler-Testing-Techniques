'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
_input_tensor = torch.Tensor([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 3, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
_output_tensor = _input_tensor.to_sparse()
print(_output_tensor)