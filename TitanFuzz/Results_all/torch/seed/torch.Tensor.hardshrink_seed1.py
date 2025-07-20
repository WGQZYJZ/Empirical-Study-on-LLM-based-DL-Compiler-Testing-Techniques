input_tensor = torch.randn(1, 2, 3)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)