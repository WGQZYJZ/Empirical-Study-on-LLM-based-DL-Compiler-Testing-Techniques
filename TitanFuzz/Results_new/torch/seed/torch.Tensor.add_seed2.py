input_data = torch.rand(2, 3)
output_data = torch.Tensor.add(input_data, input_data)
output_data = torch.Tensor.add(input_data, input_data, alpha=0.5)
output_data = torch.Tensor.add(input_data, input_data, alpha=2)