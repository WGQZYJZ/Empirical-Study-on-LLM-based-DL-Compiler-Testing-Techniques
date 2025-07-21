'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
_input_tensor = torch.randn(3, 3)
print(_input_tensor)
_index = torch.tensor([[0, 0], [1, 2]])
_source = torch.tensor([3.1415, 2.7182])
_input_tensor.put_(_index, _source, accumulate=False)
print(_input_tensor)