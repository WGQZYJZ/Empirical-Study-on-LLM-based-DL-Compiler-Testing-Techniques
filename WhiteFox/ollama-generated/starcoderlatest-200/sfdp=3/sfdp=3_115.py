
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_query = torch.nn.Linear(64, 128)
        self.linear_key   = torch.nn.Linear(64, 128)
        self.linear_value = torch.nn.Linear(64, 128)
 
    def forward(self, query):
        kq = self.linear_query(query) # Query embedding (batch, nhead, query_len, embed_dim)
        v  = self.linear_key(key)   # Key   embedding (batch, nhead, key_len, embed_dim)
        v  = torch.transpose(v, -2, -1) # (batch, nhead, embed_dim, key_len)
        qk = self.linear_value(qk) # Query key embedding (batch, nhead, query_len, embed_dim)

        output = (qk @ kq).div(64).softmax(-1).mul(v) # (batch, nhead, query_len, embed_dim)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(128, 32)
