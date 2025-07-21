'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atanh\ntorch.Tensor.atanh(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
output_data = input_data.atanh()
print('input_data: \n', input_data)
print('output_data: \n', output_data)
'\ninput_data:\ntensor([[-0.6299, -0.7549,  0.9081],\n        [-0.9077,  0.3143, -0.7790]])\noutput_data:\ntensor([[-0.7129, -0.8113,  0.9982],\n        [-0.9983,  0.3541, -0.8444]])\n'