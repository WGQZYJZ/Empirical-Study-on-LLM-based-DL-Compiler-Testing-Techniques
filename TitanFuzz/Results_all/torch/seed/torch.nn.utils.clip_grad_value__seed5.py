x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
y = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
torch.nn.utils.clip_grad_value_(x, 5)
torch.nn.utils.clip_grad_value_(y, 1)