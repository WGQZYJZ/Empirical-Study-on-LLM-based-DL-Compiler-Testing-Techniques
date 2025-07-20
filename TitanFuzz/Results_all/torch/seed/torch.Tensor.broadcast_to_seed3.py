_input_tensor = torch.randn(3, 4, 5)
_output_tensor = torch.Tensor.broadcast_to(_input_tensor, (3, 4, 5, 3))