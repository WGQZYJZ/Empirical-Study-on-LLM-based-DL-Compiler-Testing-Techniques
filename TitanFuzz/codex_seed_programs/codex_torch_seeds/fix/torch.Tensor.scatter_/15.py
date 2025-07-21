'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter_\ntorch.Tensor.scatter_(_input_tensor, dim, index, src, reduce=None)\n'
import torch
_input_tensor = torch.randint(0, 10, (3, 5))
print(_input_tensor)
_index = torch.tensor([1, 2, 0])
_src = torch.tensor([3, 4, 5])
_output_tensor = torch.zeros_like(_input_tensor)
_output_tensor.scatter_(0, _index.unsqueeze(1), _src.unsqueeze(1))
print(_output_tensor)