input_data = torch.rand(2, 3)
output_data = torch.nn.functional.gumbel_softmax(input_data, tau=1, hard=False, eps=1e-10, dim=(- 1))