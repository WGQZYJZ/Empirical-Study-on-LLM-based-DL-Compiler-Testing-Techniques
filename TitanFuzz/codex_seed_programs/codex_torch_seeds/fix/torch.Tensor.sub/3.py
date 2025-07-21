'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
tensor_a = torch.randn(2, 3)
tensor_b = torch.randn(2, 3)
sub_result = torch.sub(tensor_a, tensor_b)
print(sub_result)
sub_result = tensor_a.sub(tensor_b)
print(sub_result)
sub_result = (tensor_a - tensor_b)
print(sub_result)