'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_signed\ntorch.Tensor.is_signed(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int8)
print(input_tensor.is_signed())
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.uint8)
print(input_tensor.is_signed())
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.float32)
print(input_tensor.is_signed())
input_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.float64)
print(input_tensor.is_signed())