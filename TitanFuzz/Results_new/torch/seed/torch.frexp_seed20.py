data = torch.rand(5, 3)
(mantissa, exponent) = torch.frexp(data)