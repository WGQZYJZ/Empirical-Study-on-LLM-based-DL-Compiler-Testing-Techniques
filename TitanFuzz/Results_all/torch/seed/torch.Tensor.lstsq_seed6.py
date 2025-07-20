_input_tensor = torch.randn(3, 4, 5)
A = torch.randn(3, 4, 3)
torch.Tensor.lstsq(_input_tensor, A)