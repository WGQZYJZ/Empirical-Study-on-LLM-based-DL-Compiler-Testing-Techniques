'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
torch.set_default_dtype(torch.float32)
print(input_data)
print(input_data.dtype)