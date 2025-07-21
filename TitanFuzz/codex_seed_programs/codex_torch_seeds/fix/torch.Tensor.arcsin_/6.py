'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsin_\ntorch.Tensor.arcsin_(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
torch.Tensor.arcsin_(input_tensor)
print('The input tensor: {}'.format(input_tensor))
print("The input tensor's shape: {}".format(input_tensor.shape))
print("The input tensor's type: {}".format(input_tensor.type()))
"\nThe output:\nThe input tensor: tensor([-1.5708, -0.5236,  0.0000,  0.5236,  1.5708])\nThe input tensor's shape: torch.Size([5])\nThe input tensor's type: torch.FloatTensor\n"