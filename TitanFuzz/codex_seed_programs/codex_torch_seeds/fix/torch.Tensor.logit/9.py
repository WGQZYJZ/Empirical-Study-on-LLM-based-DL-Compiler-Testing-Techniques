'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
data = torch.randn(2, 3)
print('Input data:', data)
output = torch.Tensor.logit(data)
print('Output data:', output)
'\nExpected output:\nInput data: tensor([[-1.2559,  1.2343,  0.5998],\n        [ 0.5483,  1.8496, -0.2072]])\nOutput data: tensor([[-0.2584,  0.2273,  0.1445],\n        [ 0.1378,  0.8590, -0.1543]])\n'