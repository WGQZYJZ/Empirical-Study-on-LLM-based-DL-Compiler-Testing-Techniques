input_data = np.random.randn(100, 100)
input_data = torch.Tensor(input_data)
relu_layer = torch.nn.ReLU(inplace=False)
output = relu_layer(input_data)