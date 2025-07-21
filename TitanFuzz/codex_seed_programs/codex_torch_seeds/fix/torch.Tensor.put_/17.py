'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
index = torch.LongTensor([[2, 1], [3, 1]])
source = torch.randn(2, 2)
input_tensor.put_(index, source)
print(input_tensor)