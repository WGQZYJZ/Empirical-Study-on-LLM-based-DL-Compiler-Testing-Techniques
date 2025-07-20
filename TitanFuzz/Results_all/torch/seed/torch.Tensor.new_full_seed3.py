input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.new_full(input_tensor, size=(2, 3), fill_value=10)