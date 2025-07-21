'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
torch.Tensor.dequantize(input_tensor)
torch.Tensor.dequantize(input_tensor, scale=1.0, zero_point=0)