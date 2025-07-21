'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = _input_tensor.scatter(1, torch.tensor([[0, 1, 2], [2, 0, 1]]), torch.tensor([[1, 2, 3], [4, 5, 6]]))
print(_output_tensor)