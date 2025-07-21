'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.topk\ntorch.Tensor.topk(_input_tensor, k, dim=None, largest=True, sorted=True)\n'
import torch
_input_tensor = torch.randn(3, 5)
_topk_tuple = torch.Tensor.topk(_input_tensor, 2, dim=1, largest=True, sorted=True)
print('The input tensor is: ', _input_tensor)
print('The topk tuple is: ', _topk_tuple)