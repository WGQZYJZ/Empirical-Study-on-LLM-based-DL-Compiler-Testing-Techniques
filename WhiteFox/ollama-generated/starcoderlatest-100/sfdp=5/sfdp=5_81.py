
class Model(torch.nn.Module):
    def __init__(self, dim_q=64, dim_k=64):
        super().__init__()
        self.query = torch.nn.Linear(dim_q, dim_k)
        self.key   = torch.nn.Linear(dim_q, dim_k)

    def forward(self, query, key, value, attn_mask):
        qk = (self.query(query).view(query.size(0), query.size(1), -1) *
              self.key(key).view(key.size(0), key.size(1), -1))
        return torch.nn.functional.softmax(qk, dim=-1) @ value

# Initializing the model
m = Model(64, 64)

# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(1, 3, 64, 64)
value = torch.randn(1, 8, 64, 64)
attn_mask = torch.randn(query.size(0), query.size(2)) > 0
