x = torch.tensor([[1, 2, 3, 4, 5]], dtype=torch.float32)
y = torch.nn.ReplicationPad1d(padding=(1, 2))(x)