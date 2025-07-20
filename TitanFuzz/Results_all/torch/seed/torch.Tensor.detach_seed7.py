_input_tensor = torch.rand(2, 3, requires_grad=True)
_output_tensor = torch.Tensor.detach(_input_tensor)