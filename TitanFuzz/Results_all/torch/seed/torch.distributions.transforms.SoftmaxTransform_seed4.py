input_data = torch.randn(4, 3)
softmax_transform = torch.distributions.transforms.SoftmaxTransform(cache_size=0)
output = softmax_transform(input_data)