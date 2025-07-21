'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.share_memory_\ntorch.Tensor.share_memory_(_input_tensor, )\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor:\n{}'.format(input_tensor))
input_tensor.share_memory_()
print('input_tensor.share_memory_()\n{}'.format(input_tensor))