input_tensor = torch.randn(1, 2, 3, 4)
src = torch.randn(1, 2, 3, 4)
output_tensor = torch.Tensor.copy_(input_tensor, src, non_blocking=False)