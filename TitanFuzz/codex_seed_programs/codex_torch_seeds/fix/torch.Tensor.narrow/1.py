'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.narrow\ntorch.Tensor.narrow(_input_tensor, dimension, start, length)\n'
import torch
if True:
    input_tensor = torch.randn(2, 3, 4)
    output_tensor = input_tensor.narrow(1, 0, 2)
    print('input_tensor = \n{}'.format(input_tensor))
    print('output_tensor = \n{}'.format(output_tensor))