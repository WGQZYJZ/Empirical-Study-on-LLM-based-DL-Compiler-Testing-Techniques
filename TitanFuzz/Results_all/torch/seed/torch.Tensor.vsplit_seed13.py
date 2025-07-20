input_tensor = torch.randn(2, 3, 4)
output_tensor_list = torch.Tensor.vsplit(input_tensor, 2)
output_tensor_list = torch.Tensor.vsplit(input_tensor, [1, 2])