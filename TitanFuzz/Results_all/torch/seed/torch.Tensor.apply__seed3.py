input_tensor = torch.rand(10, 10)
output_tensor = torch.Tensor.apply_(input_tensor, (lambda x: (x * 2)))