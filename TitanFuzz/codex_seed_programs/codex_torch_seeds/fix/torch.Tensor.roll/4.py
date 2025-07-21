'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
torch.Tensor.roll(_input_tensor, shifts=1, dims=1)