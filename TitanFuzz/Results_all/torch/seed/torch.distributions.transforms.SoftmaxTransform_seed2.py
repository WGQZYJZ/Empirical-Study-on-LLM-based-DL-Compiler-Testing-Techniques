input_data = torch.randn(2, 3)
softmax_transform = torch.distributions.transforms.SoftmaxTransform(cache_size=0)
output_data = softmax_transform(input_data)