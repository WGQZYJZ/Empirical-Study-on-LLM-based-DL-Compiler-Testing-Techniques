'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.topk\ntorch.Tensor.topk(_input_tensor, k, dim=None, largest=True, sorted=True)\n'
import torch
import torch
_input_tensor = torch.rand(2, 3)
_output_tensor = _input_tensor.topk(2, dim=1, largest=True, sorted=True)
print(_output_tensor)