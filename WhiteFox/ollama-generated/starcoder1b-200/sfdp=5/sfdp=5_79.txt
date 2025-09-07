
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 64)
        self.key   = torch.nn.Linear(3, 64)
        self.value = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        query  = self.query(x1)
        key    = self.key(x1)
        value  = self.value(x1)
 
        v1 = query  @ key.transpose(-2, -1) / math.sqrt(key.size(-1))
        v2 = torch.softmax(v1, dim=-1)
        v3 = torch.dropout(v2, dropout_p, True)
        attn_weight = v3  @ value
        return attn_weight @ self.value


# Initializing the model
m = Model()


