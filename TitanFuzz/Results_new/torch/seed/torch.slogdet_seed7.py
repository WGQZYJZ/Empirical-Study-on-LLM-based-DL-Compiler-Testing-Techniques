input_tensor = torch.randn(3, 3)
(sign, log_abs_det) = torch.slogdet(input_tensor)