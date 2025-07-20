input_data = torch.rand((2, 3, 4, 5))
output = torch.hann_window(window_length=3, periodic=True, dtype=torch.float32, layout=torch.strided, device=None, requires_grad=False)