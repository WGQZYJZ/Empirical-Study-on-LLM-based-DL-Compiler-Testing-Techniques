'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.set_\ntorch.Tensor.set_(_input_tensor, source=None, storage_offset=0, size=None, stride=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
input_data.set_(torch.ones(2, 3))
print(input_data)