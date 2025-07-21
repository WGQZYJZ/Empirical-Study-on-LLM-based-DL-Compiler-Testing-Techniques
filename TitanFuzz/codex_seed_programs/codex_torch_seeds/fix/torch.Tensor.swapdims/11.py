'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapdims\ntorch.Tensor.swapdims(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(1, 2, 3)
output_tensor = torch.Tensor.swapdims(input_tensor, 0, 1)
print('input_tensor: {}'.format(input_tensor))
print('output_tensor: {}'.format(output_tensor))
'\nExpected output:\ninput_tensor: tensor([[[-0.5398, -0.1282,  0.7257],\n         [ 0.8228,  0.4608, -0.5457]]])\noutput_tensor: tensor([[[-0.5398, -0.1282,  0.7257]],\n        [[ 0.8228,  0.4608, -0.5457]]])\n'