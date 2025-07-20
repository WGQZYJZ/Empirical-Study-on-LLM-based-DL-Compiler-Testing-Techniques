input_tensor = torch.randn(2, 3)
transposed_tensor = torch.Tensor.transpose(input_tensor, 0, 1)
transposed_tensor = torch.Tensor.transpose(input_tensor, 1, 0)
transposed_tensor = torch.Tensor.transpose(input_tensor, 1, 1)