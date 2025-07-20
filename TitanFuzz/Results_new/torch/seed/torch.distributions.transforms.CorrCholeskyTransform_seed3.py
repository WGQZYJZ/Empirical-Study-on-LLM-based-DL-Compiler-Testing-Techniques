x = torch.randn(3, 3)
corr_cholesky_transform = torch.distributions.transforms.CorrCholeskyTransform(cache_size=0)
corr_cholesky_transform.inv(x)