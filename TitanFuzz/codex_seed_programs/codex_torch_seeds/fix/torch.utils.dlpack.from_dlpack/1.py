'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.dlpack.from_dlpack\ntorch.utils.dlpack.from_dlpack(ext_tensor)\n'
import torch
import torch.utils.dlpack as dlp
input_tensor = torch.rand(3, 3)
dlpack_tensor = dlp.to_dlpack(input_tensor)
print(dlpack_tensor)
tensor = dlp.from_dlpack(dlpack_tensor)
print(tensor)