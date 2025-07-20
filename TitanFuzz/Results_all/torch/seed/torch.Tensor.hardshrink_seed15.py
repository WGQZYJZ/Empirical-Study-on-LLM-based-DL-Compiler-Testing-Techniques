input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)