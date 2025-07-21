'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.dlpack.to_dlpack\ntorch.utils.dlpack.to_dlpack(tensor)\n'
import torch
from torch.utils.dlpack import from_dlpack, to_dlpack
tensor = torch.rand(2, 3)
dlpack_tensor = to_dlpack(tensor)
print(dlpack_tensor)