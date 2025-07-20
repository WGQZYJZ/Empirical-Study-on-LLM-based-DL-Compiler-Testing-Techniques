input_data = torch.randn(4, 4)
shrinked_data = torch.Tensor.hardshrink(input_data, lambd=0.5)