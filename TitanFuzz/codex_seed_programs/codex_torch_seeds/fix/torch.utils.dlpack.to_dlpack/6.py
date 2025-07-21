'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.dlpack.to_dlpack\ntorch.utils.dlpack.to_dlpack(tensor)\n'
import torch
import torch.utils.dlpack
tensor = torch.ones(2, 3)
dlpack = torch.utils.dlpack.to_dlpack(tensor)
tensor = torch.utils.dlpack.from_dlpack(dlpack)
print(tensor)