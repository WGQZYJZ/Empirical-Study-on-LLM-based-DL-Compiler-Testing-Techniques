'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unsqueeze_\ntorch.Tensor.unsqueeze_(_input_tensor, dim)\n'
import torch
input_tensor = torch.tensor([1, 2, 3, 4])
input_tensor_unsqueeze_ = input_tensor.unsqueeze_(dim=0)
print('The input tensor is: ', input_tensor)
print('The output tensor is: ', input_tensor_unsqueeze_)