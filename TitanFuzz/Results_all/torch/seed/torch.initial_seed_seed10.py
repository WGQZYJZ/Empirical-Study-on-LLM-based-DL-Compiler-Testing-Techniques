input_data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
torch.initial_seed()
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False