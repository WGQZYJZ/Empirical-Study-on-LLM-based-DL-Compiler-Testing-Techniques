'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.data_ptr\ntorch.Tensor.data_ptr(_input_tensor)\n'
import torch
x = torch.randn(3, 4)
print(x.data_ptr())