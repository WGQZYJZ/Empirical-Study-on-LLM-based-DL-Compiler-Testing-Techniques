
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, 8)
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, query, key, value, attn_mask):
        v1  = self.attn(query, key)[0]
        v2  = self.dropout(v1 + attn_mask) # Add the dropout layer after the softmax operation in MultiheadAttention
        return torch.bmm(v2, value)


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(4, 3, 800)
key   = query + torch.randn_like(query) / 100 # Initialize the key and the value with random noise. It's not required.
value = key
attn_mask = 5 * (torch.ones([4, 127], device=query.device).triu() == 1.) - math.inf
__output__  = m(query, key, value, attn_mask)

