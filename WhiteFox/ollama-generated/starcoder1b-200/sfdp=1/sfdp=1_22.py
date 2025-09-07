
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v, n_heads, mlp_dim=4096):
        super().__init__()
        self.mha = MHABlock(d_k, d_v, n_heads)
        self.fc1  = torch.nn.Linear(d_k * n_heads, mlp_dim)
        self.dropout  = torch.nn.Dropout(dropout_p)
        self.fc2  = torch.nn.Linear(mlp_dim, d_v)
 
    def forward(self, q, k, v):
        d, k = (q.size()[-2], q.size()[-1])
        m  = self.mha((q, k), d)
        output = self.dropout(torch.tanh(self.fc1(m)))
        return torch.nn.functional.dropout(self.fc2(output), p=dropout_p)


# Initializing the model
m = Model(d_k, d_v, n_heads, mlp_dim=4096)
x = torch.randn(1, 512, 64, 64)
