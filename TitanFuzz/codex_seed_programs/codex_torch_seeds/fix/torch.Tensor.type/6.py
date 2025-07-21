'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type\ntorch.Tensor.type(_input_tensor, dtype=None, non_blocking=False, **kwargs)\n'
import torch
input_data = torch.Tensor([[1, 2], [3, 4]])
print(input_data.type())
print(input_data.type(torch.FloatTensor))