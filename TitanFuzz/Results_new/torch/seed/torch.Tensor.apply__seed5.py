_input_tensor = torch.randn(3, 3)
torch.Tensor.apply_(_input_tensor, (lambda x: (x + 1)))
_input_tensor = torch.randn(3, 3)
torch.Tensor.apply_(_input_tensor, (lambda x, y: (x + y)), args=2)