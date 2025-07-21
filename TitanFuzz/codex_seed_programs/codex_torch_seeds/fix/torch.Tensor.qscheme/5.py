'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 224, 224)
qscheme = input_tensor.qscheme()
print(qscheme)