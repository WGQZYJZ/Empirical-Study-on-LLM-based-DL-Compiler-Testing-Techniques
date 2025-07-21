'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
import torch
input_tensor = torch.rand(10, 3)
print(input_tensor)
output_tensor = input_tensor.msort(dim=0)
print(output_tensor)
'\ntorch.Tensor.msort(input, dim=None, descending=False) -> Tensor\nSorts a tensor along a given dimension in ascending order by value.\nArgs:\n    input (Tensor): the tensor to sort\n    dim (int): the dimension to sort along\n    descending (bool): controls the sorting order (ascending or descending)\nReturns:\n    Tensor: the sorted tensor\n'