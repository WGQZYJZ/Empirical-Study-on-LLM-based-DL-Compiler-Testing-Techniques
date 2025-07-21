'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.neg\ntorch.Tensor.neg(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
neg_input_tensor = torch.Tensor.neg(input_tensor)
print(neg_input_tensor)