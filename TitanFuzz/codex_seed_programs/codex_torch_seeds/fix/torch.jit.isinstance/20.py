'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.isinstance\ntorch.jit.isinstance(obj, target_type)\n'
import torch
data_input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print(data_input)
torch.jit.isinstance(data_input, torch.Tensor)