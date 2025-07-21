'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.CorrCholeskyTransform\ntorch.distributions.transforms.CorrCholeskyTransform(cache_size=0)\n'
import torch
import torch.distributions as dist
import torch
import torch.distributions as dist
cov = torch.randn(3, 3)
cov = cov.mm(cov.t())
mean = torch.randn(3)
mvn = dist.MultivariateNormal(mean, cov)
sample = mvn.sample()
corr_cholesky_transform = dist.transforms.CorrCholeskyTransform()
corr_cholesky_transform(sample)