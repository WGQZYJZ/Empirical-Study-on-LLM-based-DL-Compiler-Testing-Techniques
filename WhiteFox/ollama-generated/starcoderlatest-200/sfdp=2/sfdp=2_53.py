
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(512, 2048)
        self.dropout = torch.nn.Dropout()

    def forward(self, x1, x2):
        v1 = x1 * x2
        v2 = self.matmul(v1).transpose(-1, -2)
        return self.dropout(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 512, 32, 64) # input shape : (batch size, feature dim, num_qkv, qkdim)
x2 = torch.randn(4, 2048, 32, 64) # input shape : (batch size, num_attn_heads, q, kv)
