'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.annotate\ntorch.jit.annotate(the_type, the_value)\n'
import torch
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
z = torch.jit.annotate(torch.Tensor, None)
for i in range(x.size(0)):
    for j in range(y.size(1)):
        if (z is None):
            z = (x[i, :] * y[:, j])
        else:
            z += (x[i, :] * y[:, j])
print(z)