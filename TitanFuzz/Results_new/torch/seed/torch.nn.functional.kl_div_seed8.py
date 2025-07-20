input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
target_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
kl_div_loss = torch.nn.functional.kl_div(input_data, target_data, size_average=None, reduce=None, reduction='mean', log_target=False)