_input_tensor = torch.randn(4, 4)
torch.Tensor.apply_(_input_tensor, (lambda x: (x * 2)))