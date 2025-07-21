'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(2, 3, 5, 7)
stride_dim_0 = input_tensor.stride(0)
stride_dim_1 = input_tensor.stride(1)
stride_dim_2 = input_tensor.stride(2)
stride_dim_3 = input_tensor.stride(3)
print('stride_dim_0 = ', stride_dim_0)
print('stride_dim_1 = ', stride_dim_1)
print('stride_dim_2 = ', stride_dim_2)
print('stride_dim_3 = ', stride_dim_3)