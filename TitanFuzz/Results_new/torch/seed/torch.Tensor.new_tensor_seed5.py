input_tensor = torch.randn(2, 3, 4, 5)
tensor_new = torch.Tensor.new_tensor(input_tensor, input_tensor)