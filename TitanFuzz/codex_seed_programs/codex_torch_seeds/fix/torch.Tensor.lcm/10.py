'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lcm\ntorch.Tensor.lcm(_input_tensor, other)\n'
import torch
if True:
    tensor_1 = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    tensor_2 = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(tensor_1.lcm(tensor_2))