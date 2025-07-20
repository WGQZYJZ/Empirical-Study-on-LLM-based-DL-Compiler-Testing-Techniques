input_tensor = torch.arange(1, 10).view(3, 3)
output_tensor_list = torch.Tensor.dsplit(input_tensor, 2)
output_tensor_list = torch.Tensor.dsplit(input_tensor, [2, 4])