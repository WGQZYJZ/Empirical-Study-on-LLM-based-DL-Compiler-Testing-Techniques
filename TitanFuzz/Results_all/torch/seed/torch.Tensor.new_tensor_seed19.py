_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.new_tensor(_input_tensor, _input_tensor, dtype=torch.float32, device=None, requires_grad=False)