'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.exp\ntorch.Tensor.exp(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.exp(_input_tensor)
print('The input tensor is:\n', _input_tensor)
print('The output tensor is:\n', _output_tensor)
'\nExpected output:\nThe input tensor is:\n tensor([[-0.1326,  0.9706, -0.6015],\n        [-0.8686, -1.7157, -0.6396]])\nThe output tensor is:\n tensor([[0.8743, 2.6277, 0.5404],\n        [0.4146, 0.1824, 0.5287]])\n'