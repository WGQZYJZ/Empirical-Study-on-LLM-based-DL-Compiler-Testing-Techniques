'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
import torch
x = torch.rand(3, 3)
print(x)
x = x.to_mkldnn()
print(x)