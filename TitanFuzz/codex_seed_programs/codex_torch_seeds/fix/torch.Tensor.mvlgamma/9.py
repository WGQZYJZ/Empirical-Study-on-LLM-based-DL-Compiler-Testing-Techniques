'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma\ntorch.Tensor.mvlgamma(_input_tensor, p)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: ', _input_tensor)
mvlgamma_tensor = _input_tensor.mvlgamma(2)
print('Output tensor: ', mvlgamma_tensor)
'\nExpected output:\nInput tensor:  tensor([[0.8222, 0.5113, 0.7646],\n        [0.9140, 0.9170, 0.4608]])\nOutput tensor:  tensor([[0.0781, 0.1280, 0.0860],\n        [0.0701, 0.0700, 0.1238]])\n'