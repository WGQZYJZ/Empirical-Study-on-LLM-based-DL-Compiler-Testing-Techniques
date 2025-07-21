'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
tensor_float32 = torch.tensor([1.0, 2.0, 3.0])
tensor_float64 = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float64)
torch.set_default_dtype(torch.float64)
print('The default dtype is: ', tensor_float32.dtype)
print('The dtype of tensor_float64 is: ', tensor_float64.dtype)
print('The dtype of tensor_float32 is: ', tensor_float32.dtype)