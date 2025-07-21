'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.dlpack.to_dlpack\ntorch.utils.dlpack.to_dlpack(tensor)\n'
import torch
import torch.utils.dlpack
input_data = torch.randn(2, 3)
dlpack_data = torch.utils.dlpack.to_dlpack(input_data)
print('dlpack_data: ', dlpack_data)