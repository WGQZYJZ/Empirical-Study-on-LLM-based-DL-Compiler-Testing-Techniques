'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.compiled_with_cxx11_abi\ntorch.compiled_with_cxx11_abi()\n'
import torch
data = torch.randn(10, 3)
print(data)
print(torch.compiled_with_cxx11_abi())