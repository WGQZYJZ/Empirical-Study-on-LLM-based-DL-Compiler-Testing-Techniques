input_tensor = torch.randn(1, 3, 3, 3)
output_tensor = torch.Tensor.clip(input_tensor, min=0, max=1)