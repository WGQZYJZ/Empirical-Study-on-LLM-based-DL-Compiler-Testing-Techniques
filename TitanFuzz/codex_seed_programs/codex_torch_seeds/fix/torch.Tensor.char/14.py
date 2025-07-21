'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.char\ntorch.Tensor.char(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_data = torch.randn(2, 3, 4, 5)
output_tensor = torch.Tensor.char(input_data)
print(output_tensor)