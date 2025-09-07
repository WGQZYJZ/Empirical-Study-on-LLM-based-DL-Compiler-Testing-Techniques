
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.query  = torch.nn.Linear(32, 64)
        self.key    = torch.nn.Linear(32, 64)
        self.value  = torch.nn.Linear(32, 64)
        self.dropout = torch.nn.Dropout(dropout_p)

    def forward(self, x1, x2):
        query = self.query(x1)
        key    = self.key(x2)
        value  = self.value(x2)

        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        attn_mask  = torch.softmax(qk, dim=-1)  # Compute the softmax of the scaled dot product
        attn_weight = self.dropout(attn_mask)

        return attn_weight @ value


# Initializing the model
m = Model()


