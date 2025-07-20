_input_tensor = torch.randn(4, 2, 3)
_output_tensor = torch.Tensor.broadcast_to(_input_tensor, (4, 2, 3, 4))