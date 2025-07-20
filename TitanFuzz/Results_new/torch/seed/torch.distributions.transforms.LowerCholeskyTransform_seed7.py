input_data = torch.randn(3, 3)
transform = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)
output_data = transform(input_data)