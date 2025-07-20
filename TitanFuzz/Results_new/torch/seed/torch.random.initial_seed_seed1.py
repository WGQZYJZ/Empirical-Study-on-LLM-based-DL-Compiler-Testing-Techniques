np.random.seed(1)
input_data = np.random.randn(10, 3)
torch.random.initial_seed()
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False