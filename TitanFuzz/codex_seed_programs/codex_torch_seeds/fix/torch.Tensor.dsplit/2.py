'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dsplit\ntorch.Tensor.dsplit(_input_tensor, split_size_or_sections)\n'
import torch
inp_tensor = torch.arange(0, 16).reshape(2, 2, 4)
out_tensor = inp_tensor.dsplit(2)
print('The input tensor is: ', inp_tensor)
print('The output tensor is: ', out_tensor)