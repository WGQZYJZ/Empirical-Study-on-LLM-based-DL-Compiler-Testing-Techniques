'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.dlpack.to_dlpack\ntorch.utils.dlpack.to_dlpack(tensor)\n'
import torch
import torch.utils.dlpack
x = torch.rand(2, 3)
print('Input data: ', x)
dlpack_tensor = torch.utils.dlpack.to_dlpack(x)
print('DLPack tensor: ', dlpack_tensor)
print('DLPack tensor type: ', type(dlpack_tensor))