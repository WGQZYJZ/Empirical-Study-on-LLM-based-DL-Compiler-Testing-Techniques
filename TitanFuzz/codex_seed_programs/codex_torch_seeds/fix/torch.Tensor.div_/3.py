'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value, *, rounding_mode=None)\n'
import torch
print(torch.__version__)
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])
print(tensor_a.div(tensor_b))
print(tensor_a.div_(tensor_b))