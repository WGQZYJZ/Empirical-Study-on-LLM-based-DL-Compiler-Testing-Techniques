_input_tensor = torch.randn(3, 3)
other = torch.randn(3, 3)
_output_tensor = torch.Tensor.igamma(_input_tensor, other)