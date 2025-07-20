input_tensor = torch.randn(2, 3)
retains_grad_result = torch.Tensor.retains_grad(input_tensor, True)