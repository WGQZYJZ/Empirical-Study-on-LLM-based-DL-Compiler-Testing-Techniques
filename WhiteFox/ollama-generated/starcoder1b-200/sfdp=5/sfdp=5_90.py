
class Model(torch.nn.Module):
    def __init__(self, key_dim=64, value_dim=128, nhead=8, dim_feedforward=512, dropout=0):
        super().__init__()

        self.dropout = torch.nn.Dropout(dropout)

        self.linear_query = torch.nn.Linear(key_dim + dim_feedforward, value_dim)
        self.linear_key = torch.nn.Linear(key_dim + dim_feedforward, value_dim)
        self.linear_value = torch.nn.Linear(value_dim, value_dim)

        self.attn_head  = torch.nn.Linear(nhead * value_dim, 1)

    def forward(self, x):
        h   = self.dropout(x).contiguous()
        k   = self.linear_query(h)
        key = self.linear_key(h)

        v   = self.linear_value(h)
        out = self.attn_head(torch.matmul(k, v))  # Compute the dot product of k and v

        attn_weight = F.softmax(out, dim=-1)
        out        = torch.matmul(attn_weight, v)    # Compute the output for attention calculation
        return self.dropout(out) + h


# Initializing the model
m = Model()

