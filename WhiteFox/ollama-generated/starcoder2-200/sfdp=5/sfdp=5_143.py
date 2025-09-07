
class Model(torch.nn.Module):
    def __init__(self, query=256, key=1024, value=2304):
        super().__init__()
        self.query = torch.nn.Linear(query, 1)
        self.key = torch.nn.Linear(key, query)
        self.value = torch.nn.Linear(value, query)

    def forward(self, x):
        attn_mask = torch.zeros(x.size()).triu_(1).tril() / math.sqrt(query.size(-1))

        v  = self.query @ self.key.transpose(-2,-1) 
        v += attn_mask
        attn_weight  = torch.softmax(v, dim=-1)

        return v @ self.value.transpose(-2,-1), attn_weight

# Initializing the model
m = Model()

