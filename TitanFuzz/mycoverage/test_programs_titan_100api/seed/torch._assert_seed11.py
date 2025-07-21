input_data = torch.Tensor([1, 2, 3, 4, 5])
torch._assert(torch.all((input_data > 0)), 'Input data must be positive')