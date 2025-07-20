input_data = Variable(torch.Tensor([[1, 2, 4, 8], [1, 2, 4, 8]]))
target_data = Variable(torch.Tensor([[1, 2, 4, 8], [1, 2, 4, 8]]))
kl_div_loss = torch.nn.functional.kl_div(input_data, target_data)