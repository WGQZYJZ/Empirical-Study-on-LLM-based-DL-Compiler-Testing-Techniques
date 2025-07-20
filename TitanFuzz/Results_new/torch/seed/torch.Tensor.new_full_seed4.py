_input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.new_full(_input_tensor, size=(2, 3), fill_value=2, dtype=torch.float32)