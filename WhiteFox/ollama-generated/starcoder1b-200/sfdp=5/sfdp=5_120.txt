
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead, dropout=0.1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_model, nhead)
        self.ln = torch.nn.LayerNorm(d_model)
        self.dropout = torch.nn.Dropout(p=dropout)
 
    def forward(self, query, key, value):
        # Normalize input
        query = self.ln(query)
        key = self.ln(key)
        # Compute dot product
        attn_weight = self.attn(query, key, value)  # [batch x head x seq x seq]
        attn_weight = torch.softmax(attn_weight, dim=-1)  # [batch x head x seq x seq]
        # Compute the dropout output
        attn_weight = self.dropout(attn_weight, training=self.training)
        # Compute value product
        out = torch.matmul(attn_weight, value)
        return out


# Initializing the model
m = Model()


