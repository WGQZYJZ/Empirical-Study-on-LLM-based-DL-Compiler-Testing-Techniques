'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
_neg_tensor = torch.Tensor.neg(_input_tensor)
print('The input tensor is:', _input_tensor)
print('The neg tensor is:', _neg_tensor)