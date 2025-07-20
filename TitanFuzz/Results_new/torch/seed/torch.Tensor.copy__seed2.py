_input_tensor = torch.randn(2, 3)
src = torch.randn(2, 3)
torch.Tensor.copy_(_input_tensor, src, non_blocking=False)