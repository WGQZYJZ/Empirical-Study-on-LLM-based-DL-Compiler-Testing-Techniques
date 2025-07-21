'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resize_\ntorch.Tensor.resize_(_input_tensor, *sizes, memory_format=torch.contiguous_format)\n'
import torch
tensor = torch.randn(2, 3, 4)
print('tensor = ', tensor)
resize_tensor = tensor.resize_(3, 2)
print('resize_tensor = ', resize_tensor)