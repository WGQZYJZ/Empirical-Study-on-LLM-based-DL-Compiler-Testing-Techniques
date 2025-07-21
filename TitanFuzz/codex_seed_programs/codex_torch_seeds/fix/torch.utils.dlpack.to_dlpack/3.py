'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.dlpack.to_dlpack\ntorch.utils.dlpack.to_dlpack(tensor)\n'
import torch
from torch.utils import dlpack
x = torch.randn(10, 3)
x_dlpack = dlpack.to_dlpack(x)
print(x_dlpack)
print(type(x_dlpack))
x_recover = dlpack.from_dlpack(x_dlpack)
print(x_recover)
print(type(x_recover))