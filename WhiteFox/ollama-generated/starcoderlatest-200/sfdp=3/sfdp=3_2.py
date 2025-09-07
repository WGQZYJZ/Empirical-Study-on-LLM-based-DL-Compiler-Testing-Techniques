
class Model(torch.nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.query = torch.nn.Linear(hidden_dim * 2, hidden_dim)
        self.key   = torch.nn.Linear(hidden_dim * 2, hidden_dim)
        self.value = torch.nn.Linear(hidden_dim * 2, hidden_dim)
 
    def forward(self, q, k, v):
        scaled_qk = torch.matmul(q, k.transpose(-2, -1))
        softmax_qk = scaled_qk.softmax(dim=-1)
        output      = torch.matmul(dropout_qk, value)
        return output
# Initializing the model
m = Model(4096)


# Inputs to the model
q = torch.randn(1, 32, 8192)
k = torch.randn(1, 32, 8192)
v = torch.randn(1, 32, 8192)
