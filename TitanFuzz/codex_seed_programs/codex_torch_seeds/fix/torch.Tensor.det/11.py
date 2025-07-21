'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
input_tensor = torch.randint(10, (2, 2), dtype=torch.float32)
det_ = input_tensor.det()
print('The determinant of the input tensor is: ', det_)