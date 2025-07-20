input_data = torch.randn(3, 5)
(q_out, r_out) = torch.geqrf(input_data)