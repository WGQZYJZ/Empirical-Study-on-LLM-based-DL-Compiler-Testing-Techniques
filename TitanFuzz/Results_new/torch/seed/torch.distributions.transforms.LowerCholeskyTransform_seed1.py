input_data = torch.rand(size=(2, 2))
transform = torch.distributions.transforms.LowerCholeskyTransform(cache_size=0)
output_data = transform(input_data)