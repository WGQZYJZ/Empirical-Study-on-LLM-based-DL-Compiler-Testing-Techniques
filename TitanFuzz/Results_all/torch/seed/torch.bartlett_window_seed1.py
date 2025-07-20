window_length = 10
periodic = True
dtype = torch.float32
device = torch.device('cpu')
requires_grad = False
output = torch.bartlett_window(window_length, periodic, dtype=dtype, device=device, requires_grad=requires_grad)