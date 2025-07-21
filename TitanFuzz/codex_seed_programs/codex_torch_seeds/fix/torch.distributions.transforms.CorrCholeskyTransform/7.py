'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.CorrCholeskyTransform\ntorch.distributions.transforms.CorrCholeskyTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
batch_size = 5
input_size = 3
x = torch.rand(batch_size, input_size)
transform = transforms.CorrCholeskyTransform()
y = transform(x)
print(y)