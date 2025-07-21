'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
input_qscheme = torch.rand(2, 3, 4, 5, dtype=torch.float)
output_qscheme = input_qscheme.qscheme()
print('Output of qscheme is: ', output_qscheme)