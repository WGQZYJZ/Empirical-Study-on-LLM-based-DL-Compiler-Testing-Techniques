'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
sign_data = input_data.sign()
print(sign_data)