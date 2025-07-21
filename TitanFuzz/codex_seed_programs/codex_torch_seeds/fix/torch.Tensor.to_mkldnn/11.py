'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
input_tensor.to_mkldnn()
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor, _dtype, _layout)\n'
import torch
import torch
input_tensor = torch.rand(3, 3)
dtype = torch.int32
layout = torch.strided
input_tensor.to_mkldnn(dtype, layout)