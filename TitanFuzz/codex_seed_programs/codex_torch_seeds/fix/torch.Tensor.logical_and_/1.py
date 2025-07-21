'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and_\ntorch.Tensor.logical_and_(_input_tensor, other)\n'
import torch
tensor_1 = torch.tensor([[False, False, False], [True, True, True], [False, False, False]])
tensor_2 = torch.tensor([[False, True, False], [False, True, False], [False, True, False]])
torch.Tensor.logical_and_(tensor_1, tensor_2)
print(tensor_1)