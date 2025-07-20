input_tensor = torch.rand(2, 3, dtype=torch.float32)
torch.nn.init.ones_(input_tensor)
input_tensor = torch.rand(2, 3, dtype=torch.float32)
torch.nn.init.zeros_(input_tensor)