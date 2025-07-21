input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
torch._assert((input_data.dim() == 1), 'input_data must be 1-dimensional')