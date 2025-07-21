'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_2 = torch.tensor([[1, 1, 1], [2, 2, 2]])
result = torch.broadcast_tensors(tensor_1, tensor_2)
print(result)
assert (result[0] == tensor_1).all()
assert (result[1] == tensor_2).all()