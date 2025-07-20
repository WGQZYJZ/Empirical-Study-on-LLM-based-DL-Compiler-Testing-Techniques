input_tensor = torch.rand(1000)
histogram = torch.Tensor.histogram(input_tensor, 10, 0, 1)