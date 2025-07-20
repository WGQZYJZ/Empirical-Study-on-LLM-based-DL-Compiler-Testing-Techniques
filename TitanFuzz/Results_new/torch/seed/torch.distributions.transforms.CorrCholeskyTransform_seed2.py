input = torch.randn(2, 3)
transform = torch.distributions.transforms.CorrCholeskyTransform(cache_size=0)
output = transform(input)