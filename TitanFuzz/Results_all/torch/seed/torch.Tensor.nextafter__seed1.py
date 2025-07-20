_input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
_out_tensor = torch.Tensor.nextafter_(_input_tensor, other)