'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pinverse\ntorch.Tensor.pinverse(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
pinverse_tensor = input_tensor.pinverse()
print('input_tensor:', input_tensor)
print('pinverse_tensor:', pinverse_tensor)
'\nExpected output:\ninput_tensor: tensor([[1., 2.],\n        [3., 4.]])\npinverse_tensor: tensor([[-2.0000,  1.0000],\n        [ 1.5000, -0.5000]])\n'