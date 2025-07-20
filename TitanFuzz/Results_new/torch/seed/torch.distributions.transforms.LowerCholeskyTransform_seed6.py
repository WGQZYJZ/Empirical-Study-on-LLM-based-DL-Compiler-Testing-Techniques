x = torch.randn(3, 3)
lct = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)
y = lct(x)