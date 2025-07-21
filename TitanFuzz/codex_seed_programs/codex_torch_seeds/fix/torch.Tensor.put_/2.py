'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
inp_tensor = torch.Tensor([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(inp_tensor)
torch.Tensor.put_(inp_tensor, [0, 1, 2, 3, 4, 5, 6, 7, 8], [11, 22, 33, 44, 55, 66, 77, 88, 99])
print(inp_tensor)
torch.Tensor.put_(inp_tensor, [0, 1, 2, 3, 4, 5, 6, 7, 8], [11, 22, 33, 44, 55, 66, 77, 88, 99], accumulate=True)
print(inp_tensor)