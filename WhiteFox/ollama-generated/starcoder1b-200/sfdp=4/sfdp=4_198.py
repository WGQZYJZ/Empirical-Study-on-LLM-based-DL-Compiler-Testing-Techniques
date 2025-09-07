
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(64, 32)
        self.key   = torch.nn.Linear(64, 32)
        self.value = torch.nn.Linear(64, 32)

    def forward(self, query, key, value):
        qv_mul  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size(-1))
        vq_mul  = value @ attn_mask * 0.5
        output  = torch.einsum('bc,bc->bc', qv_mul, vq_mul)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(1, 32, 64, 64)
key    = torch.randn(1, 32, 64, 64)
value  = torch.randn(1, 32, 64, 64)
