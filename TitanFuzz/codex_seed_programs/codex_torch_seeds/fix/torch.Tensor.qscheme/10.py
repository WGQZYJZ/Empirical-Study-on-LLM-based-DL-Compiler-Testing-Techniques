'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
qscheme = input_tensor.qscheme()
print('The quantization scheme of the tensor is: {}'.format(qscheme))