input_tensor = torch.arange(1, 11, dtype=torch.float)
torch.Tensor.divide_(input_tensor, 2)
torch.Tensor.divide_(input_tensor, 2, rounding_mode='floor')
torch.Tensor.divide_(input_tensor, 2, rounding_mode='ceil')
torch.Tensor.divide_(input_tensor, 2, rounding_mode='trunc')