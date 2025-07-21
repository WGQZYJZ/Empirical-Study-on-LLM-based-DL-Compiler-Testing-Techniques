'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.as_tensor\ntorch.as_tensor(data, dtype=None, device=None)\n'
import torch
data = [[1, 2], [3, 4]]
tensor_data = torch.as_tensor(data)
print('tensor_data: ', tensor_data)
print('tensor_data.dtype: ', tensor_data.dtype)
print('tensor_data.device: ', tensor_data.device)
print('tensor_data.layout: ', tensor_data.layout)
tensor_data = torch.tensor(data)
print('tensor_data: ', tensor_data)
print('tensor_data.dtype: ', tensor_data.dtype)
print('tensor_data.device: ', tensor_data.device)
print('tensor_data.layout: ', tensor_data.layout)