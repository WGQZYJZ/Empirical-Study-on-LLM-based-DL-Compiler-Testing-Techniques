_input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.new_full(_input_tensor, size=(3, 2), fill_value=0.5)