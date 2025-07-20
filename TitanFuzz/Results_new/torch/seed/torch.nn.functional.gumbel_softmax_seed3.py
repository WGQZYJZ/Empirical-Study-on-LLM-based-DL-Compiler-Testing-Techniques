input_data = torch.randn(4, 4)
input_data.requires_grad = True
output = torch.nn.functional.gumbel_softmax(input_data, tau=1, hard=False, eps=1e-10, dim=(- 1))
output.backward(torch.ones(output.size()))