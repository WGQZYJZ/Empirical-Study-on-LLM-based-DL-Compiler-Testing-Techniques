'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_scatter_\ntorch.Tensor.masked_scatter_(_input_tensor, mask, source\n'
import torch
_input_tensor = torch.randn(3, 4)
_mask = torch.tensor([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 0]])
_source = torch.tensor([[(- 1), (- 1), (- 1), (- 1)], [(- 1), (- 1), (- 1), (- 1)], [(- 1), (- 1), (- 1), (- 1)]])
torch.Tensor.masked_scatter_(_input_tensor, _mask, _source)
print('input_tensor: ', _input_tensor)
print('mask: ', _mask)
print('source: ', _source)