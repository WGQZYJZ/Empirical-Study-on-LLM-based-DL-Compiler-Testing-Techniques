input_tensor = torch.arange(0, 12)
input_tensor = input_tensor.view(3, 4)
output_tensor_list = torch.Tensor.vsplit(input_tensor, 2)