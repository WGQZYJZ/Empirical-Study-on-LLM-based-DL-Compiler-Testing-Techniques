
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(d_model, d_k) # Query
        self.v = torch.nn.Linear(d_model, d_v) # Value

    def forward(self, x):
        query = self.qk(x)  # Compute the query of the input with shape [batch_size, length, d_k]
        value = self.v(x)  # Compute the value with shape [batch_size, length, d_v]
        return torch.matmul(query, value), x


# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(1, 512, dtype=torch.double)
k1 = torch.randn(1, 128, 64, dtype=torch.double)
v1 = torch.randn(1, 256, 32, dtype=torch.double)
__output, _ = m(q1, k1, v1)

