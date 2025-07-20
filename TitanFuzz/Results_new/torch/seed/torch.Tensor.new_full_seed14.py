_input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.new_full(_input_tensor, size=(2, 2), fill_value=3.0)