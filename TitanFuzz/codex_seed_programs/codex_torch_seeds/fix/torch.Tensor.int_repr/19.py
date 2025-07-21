'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int_repr\ntorch.Tensor.int_repr(_input_tensor)\n'
import torch
if True:
    input_tensor = torch.randint(0, 255, (2, 3, 4), dtype=torch.uint8)
    print('input_tensor: ', input_tensor)
    print('input_tensor.int_repr(): ', input_tensor.int_repr())