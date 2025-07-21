'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.matrix_exp\ntorch.Tensor.matrix_exp(_input_tensor)\n'
import torch
inp_data = torch.randn(3, 3)
print(inp_data)
out_data = torch.Tensor.matrix_exp(inp_data)
print(out_data)