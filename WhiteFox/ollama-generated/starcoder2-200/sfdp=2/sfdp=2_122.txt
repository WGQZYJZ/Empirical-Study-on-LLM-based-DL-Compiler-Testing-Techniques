
class Model(torch.nn.Module):
    def __init__(self,
                 nhead=8,
                 dim=2048,
                 dropout=0.1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(dim,
                                                 num_heads=nhead)
        self.dropout  = torch.nn.Dropout(p=dropout)

    def forward(self, query, key, value):
        v1  = self.attn(query,
                        key,
                        value)[0] # Apply attention to the query, key and value tensors
        v2  = self.dropout(v1) # Apply dropout to the output of attention
        return v2


# Initializing the model
m  = Model()

# Inputs for the model
x_query = torch.randn(8, 50, 2048)
x_key   = torch.randn(3, 16777216).to(dtype=torch.int32) # Make sure that the key is an integer array
x_value = x_query.clone() * 1000 + x_query
__output__  = m(x_query,
                x_key,
                x_value)

