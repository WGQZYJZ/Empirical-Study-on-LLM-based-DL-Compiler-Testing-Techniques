input_tensor = torch.randn(3, 3)
step_function = torch.Tensor.heaviside(input_tensor, torch.tensor(0.5))