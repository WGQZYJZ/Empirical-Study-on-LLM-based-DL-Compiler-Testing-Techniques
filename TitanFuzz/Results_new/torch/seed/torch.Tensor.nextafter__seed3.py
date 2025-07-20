_input_tensor = torch.rand(3, 3)
other = torch.rand(3, 3)
torch.Tensor.nextafter_(_input_tensor, other)