'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bool\ntorch.Tensor.bool(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
if True:
    input_tensor = torch.randn(3, 3, dtype=torch.float)
    print('input_tensor: ', input_tensor)
    output_tensor = input_tensor.bool()
    print('output_tensor: ', output_tensor)