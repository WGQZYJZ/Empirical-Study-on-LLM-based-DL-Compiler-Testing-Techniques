'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn_like\ntorch.randn_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], dtype=torch.float32)
print(input_data)
output_data = torch.randn_like(input_data)
print(output_data)