input_tensor = torch.rand((4, 4))
output_tensor = torch.Tensor.heaviside(input_tensor, values=0.5)