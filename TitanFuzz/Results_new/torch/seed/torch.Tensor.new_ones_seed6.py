input_tensor = torch.randn(1, 3)
output_tensor = torch.Tensor.new_ones(input_tensor, (1, 3), dtype=torch.float32, device=None, requires_grad=False)