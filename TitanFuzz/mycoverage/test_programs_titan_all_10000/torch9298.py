import torch
from torch import nn
from torch.autograd import Variable
A = torch.randn(3, 3)
pinv_A = torch.linalg.pinv(A)
(U, S, V) = torch.svd(A)
mask = (S > 1e-15).type(torch.bool)
S_inv = torch.zeros(A.shape[0], A.shape[1])
S_inv[mask] = (1.0 / S[mask])
pinv_A_2 = torch.mm(V.t(), torch.mm(S_inv.t(), U.t()))