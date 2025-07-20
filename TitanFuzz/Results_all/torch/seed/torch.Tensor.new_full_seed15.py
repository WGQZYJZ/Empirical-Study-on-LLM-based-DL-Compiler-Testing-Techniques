_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.new_full(_input_tensor, size=(4, 4), fill_value=2.0)