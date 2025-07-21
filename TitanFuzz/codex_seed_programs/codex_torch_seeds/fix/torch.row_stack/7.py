'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.row_stack\ntorch.row_stack(tensors, *, out=None)\n'
import torch
input1 = torch.rand(3, 3)
input2 = torch.rand(3, 3)
input3 = torch.rand(3, 3)
output = torch.row_stack((input1, input2, input3))
print(output)
output2 = torch.zeros(9, 3)
torch.row_stack((input1, input2, input3), out=output2)
print(output2)