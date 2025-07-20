_input_tensor = torch.randn(3, 5)
_output_tensor = torch.Tensor.new_full(_input_tensor, 3, fill_value=10)