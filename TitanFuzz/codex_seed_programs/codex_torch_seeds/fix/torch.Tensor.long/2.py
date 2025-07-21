'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.long\ntorch.Tensor.long(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print(input_tensor)
result_tensor = torch.Tensor.long(input_tensor)
print(result_tensor)