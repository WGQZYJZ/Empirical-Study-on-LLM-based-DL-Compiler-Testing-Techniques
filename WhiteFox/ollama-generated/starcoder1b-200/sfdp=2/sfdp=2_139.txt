
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_fc1 = torch.nn.Linear(d_model, d_qk * 4)
        self.v = torch.nn.Parameter(torch.zeros((d_v, 1)))

    def forward(self, x):
        q, k, v = map(lambda x: x.reshape(x.shape[:-2] + (1,)) if x.ndimension() == 3 else x,
                       self.qkv_fc1(x).chunk(3, dim=-1))
        return (q @ k.transpose(-2, -1)).div(torch.sqrt(k.size(-1))) @ v


# Initializing the model
m = Model()


# Inputs to the model
q  = torch.randn(1, 5, 3, 3)  # Shape: (batch_size, seq_len, d_model)
k  = torch.randn(2, 5, 3, 3)  # Shape: (batch_size, seq_len, d_model)
v  = torch.randn(1, 5, 3, 3)  # Shape: (batch_size, seq_len, d_model)
