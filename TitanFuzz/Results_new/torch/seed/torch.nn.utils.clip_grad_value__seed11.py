data = np.random.rand(2, 3)
data = torch.from_numpy(data)
clip_value = 0.5
torch.nn.utils.clip_grad_value_(data, clip_value)