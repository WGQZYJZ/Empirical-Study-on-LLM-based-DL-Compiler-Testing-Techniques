input_tensor = torch.randn(4, 4, 4)
output_tensor_list = torch.Tensor.dsplit(input_tensor, 2)