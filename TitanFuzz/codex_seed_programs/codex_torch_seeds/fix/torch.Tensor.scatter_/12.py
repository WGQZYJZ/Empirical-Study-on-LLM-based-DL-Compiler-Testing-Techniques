'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
_input_tensor = torch.randn(3, 5)
print('_input_tensor: ', _input_tensor)
_index_tensor = torch.tensor([[4, 5, 4, 1], [3, 3, 2, 4]])
_src_tensor = torch.tensor([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]])
_output_tensor = torch.Tensor.scatter_(_input_tensor, 0, _index_tensor, _src_tensor)
print('_output_tensor: ', _output_tensor)