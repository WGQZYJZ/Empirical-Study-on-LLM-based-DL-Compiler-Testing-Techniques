'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.as_strided\ntorch.Tensor.as_strided(_input_tensor, size, stride, storage_offset=0)\n'
import torch
tensor_1 = torch.arange(1, 11)
print(tensor_1)
tensor_2 = torch.Tensor.as_strided(tensor_1, (4, 3), (2, 2))
print(tensor_2)