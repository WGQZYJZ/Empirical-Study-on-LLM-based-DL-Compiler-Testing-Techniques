"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.qr\ntorch.linalg.qr(A, mode='reduced', *, out=None)\n"
import torch
A = torch.randn(3, 3)
(Q, R) = torch.linalg.qr(A)
print('Q:', Q)
print('R:', R)
print('diag(R):', R.diag())
print('upper tri(R):', R.triu())
print('lower tri(R):', R.tril())
print('upper tri(Q):', Q.triu())
print('lower tri(Q):', Q.tril())
print('upper tri(Q):', Q.triu())
print('lower tri(Q):', Q.tril())