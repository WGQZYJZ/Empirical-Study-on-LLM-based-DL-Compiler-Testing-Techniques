'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical_\ntorch.Tensor.conj_physical_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
torch.Tensor.conj_physical_(input_tensor)
print(input_tensor)