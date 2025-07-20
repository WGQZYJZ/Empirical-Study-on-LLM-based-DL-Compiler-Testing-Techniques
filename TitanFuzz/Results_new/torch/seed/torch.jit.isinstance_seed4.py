obj = torch.randn(3, 4)
target_type = torch.Tensor
result = torch.jit.isinstance(obj, target_type)