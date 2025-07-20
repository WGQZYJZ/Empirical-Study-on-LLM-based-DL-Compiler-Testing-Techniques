_input_tensor = torch.randn(2, 3, 4)
src = torch.randn(2, 3, 4)
torch.Tensor.copy_(_input_tensor, src, non_blocking=False)