input_tensor = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
output_tensor = torch.Tensor.hardshrink(input_tensor, lambd=0.5)