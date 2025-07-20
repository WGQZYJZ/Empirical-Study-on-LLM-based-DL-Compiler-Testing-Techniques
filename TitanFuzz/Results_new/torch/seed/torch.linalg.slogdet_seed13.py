input_data = torch.randn(3, 3)
(sign, logdet) = torch.linalg.slogdet(input_data)