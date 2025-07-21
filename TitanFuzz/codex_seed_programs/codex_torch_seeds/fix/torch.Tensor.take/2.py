'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
indices = torch.tensor([0, 2])
output_tensor = torch.Tensor.take(_input_tensor, indices)
print('The input tensor is: ', _input_tensor)
print('The indices is: ', indices)
print('The output tensor is: ', output_tensor)