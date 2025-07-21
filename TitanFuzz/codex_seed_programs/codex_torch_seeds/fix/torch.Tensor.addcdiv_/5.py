'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv_\ntorch.Tensor.addcdiv_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
tensor_one = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tensor_two = torch.tensor([5, 4, 3, 2, 1, 10, 9, 8, 7, 6])
tensor_three = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tensor_one.addcdiv_(tensor_two, tensor_three, value=1)
print(tensor_one)