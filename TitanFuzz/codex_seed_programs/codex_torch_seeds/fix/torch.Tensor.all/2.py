'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.all\ntorch.Tensor.all(_input_tensor, dim=None, keepdim=False)\n'
import torch
input_tensor_1 = torch.tensor([1, 2, 3, 4, 5])
input_tensor_2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor_1 = torch.Tensor.all(input_tensor_1, dim=None, keepdim=False)
output_tensor_2 = torch.Tensor.all(input_tensor_2, dim=None, keepdim=False)
output_tensor_3 = torch.Tensor.all(input_tensor_2, dim=1, keepdim=False)
output_tensor_4 = torch.Tensor.all(input_tensor_2, dim=1, keepdim=True)
print('The result of torch.Tensor.all(input_tensor_1, dim=None, keepdim=False) is:', output_tensor_1)