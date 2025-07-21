'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nextafter\ntorch.Tensor.nextafter(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([1, 2, 3], dtype=torch.float64)
other = torch.tensor([4, 5, 6], dtype=torch.float64)
print(input_tensor.nextafter(other))