_input_tensor = torch.randn(1, 3, 3, 3)
_output_tensor = torch.Tensor.new_full(_input_tensor, size=(1, 3, 3, 3), fill_value=10, dtype=torch.float32, device=None, requires_grad=False)