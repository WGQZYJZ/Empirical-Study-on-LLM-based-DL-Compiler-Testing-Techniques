input_tensor = torch.randn((1, 3, 3), requires_grad=True)
output_tensor = torch.Tensor.detach_(input_tensor)