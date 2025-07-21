'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.dlpack.to_dlpack\ntorch.utils.dlpack.to_dlpack(tensor)\n'
import torch
import torch.utils.dlpack
import numpy as np
data = torch.rand(2, 3)
print(data)
dlpack = torch.utils.dlpack.to_dlpack(data)
print(dlpack)
print(type(dlpack))
data_np = np.array(dlpack)
print(data_np)