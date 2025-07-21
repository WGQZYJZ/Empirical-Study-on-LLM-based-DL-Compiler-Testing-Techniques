'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
import torch
_input_tensor = torch.arange(0, 12).reshape(3, 4)
torch.Tensor.roll(_input_tensor, shifts=1, dims=1)