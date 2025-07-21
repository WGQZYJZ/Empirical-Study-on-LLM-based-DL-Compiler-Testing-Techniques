'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.roll\ntorch.Tensor.roll(_input_tensor, shifts, dims)\n'
import torch
_input_tensor = torch.Tensor([[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]])
torch.Tensor.roll(_input_tensor, shifts=(- 1), dims=2)
print('The input tensor is:')
print(_input_tensor)
print('The output tensor is:')
print(torch.Tensor.roll(_input_tensor, shifts=(- 1), dims=2))