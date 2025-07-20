_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.broadcast_to(_input_tensor, (3, 2, 3))