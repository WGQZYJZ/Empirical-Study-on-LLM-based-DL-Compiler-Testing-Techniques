input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.tensor(input_data, dtype=torch.float32)
softmax = torch.distributions.transforms.SoftmaxTransform(cache_size=0)