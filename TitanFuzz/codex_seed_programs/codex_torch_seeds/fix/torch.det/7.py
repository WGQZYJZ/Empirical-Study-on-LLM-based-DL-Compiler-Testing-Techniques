'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.det\ntorch.det(input)\n'
import torch
from torch.autograd import Variable
A = torch.Tensor([[1, 2], [3, 4]])
A = Variable(A, requires_grad=True)
print(torch.det(A))
B = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = Variable(B, requires_grad=True)
print(torch.det(B))
C = torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
C = Variable(C, requires_grad=True)
print(torch.det(C))