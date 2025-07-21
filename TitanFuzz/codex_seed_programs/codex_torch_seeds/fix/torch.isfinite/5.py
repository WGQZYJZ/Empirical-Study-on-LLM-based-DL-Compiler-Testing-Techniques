'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isfinite\ntorch.isfinite(input)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
print(input_data)
result = torch.isfinite(input_data)
print(result)