input_data = torch.randn(1, 3, 3)
softmax2d = torch.nn.Softmax2d()
output = softmax2d(input_data)