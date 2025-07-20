input_tensor = torch.rand(5, 5, requires_grad=True)
output_tensor = torch.Tensor.pow_(input_tensor, 2)