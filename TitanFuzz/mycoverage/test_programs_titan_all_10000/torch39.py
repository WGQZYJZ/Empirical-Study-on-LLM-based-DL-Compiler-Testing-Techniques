import torch
from torch import nn
from torch.autograd import Variable
A = np.array([[4, 12, (- 16)], [12, 37, (- 43)], [(- 16), (- 43), 98]])
A = torch.from_numpy(A)
A = A.float()
L = torch.linalg.cholesky(A)