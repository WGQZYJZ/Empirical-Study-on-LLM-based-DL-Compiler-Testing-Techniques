input_tensor = torch.randn(3, 3)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)