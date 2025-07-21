'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log2\ntorch.Tensor.log2(_input_tensor)\n'
import torch
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.Tensor(data)
print(tensor)
print(tensor.log2())