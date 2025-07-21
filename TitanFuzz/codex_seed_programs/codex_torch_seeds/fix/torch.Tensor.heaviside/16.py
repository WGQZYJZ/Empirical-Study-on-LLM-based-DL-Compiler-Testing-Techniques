'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.tensor([0.1, (- 0.1), 0.3, (- 0.3)])
output_tensor = input_tensor.heaviside(values=[1.0, 2.0])
print('The input tensor is: ', input_tensor)
print('The output tensor is: ', output_tensor)
'\nThe input tensor is:  tensor([ 0.1000, -0.1000,  0.3000, -0.3000])\nThe output tensor is:  tensor([1., 1., 2., 1.])\n'