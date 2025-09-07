
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads=8)
 
    def forward(self, query, key, value):
        scaled_qk  = self.attn(query, key)[0] * scale_factor # Compute the dot product of the query and key tensors 
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk= torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output    = dropout_qk @ value  # Compute the dot product of the dropout output and the value tensor 
        return output


# Initializing the model
m  = Model()


# Inputs to the model
query1 = torch.randn(4, 8, embed_dim)  # query in shape [batch, heads, dim]
key    = torch.randn(50, 8, embed_dim)  # key in shape [batch, heads, dim]
value  = torch.randn(6, 8 * embed_dim) # value in shape [batch, heads*dim]


# Inputs to the model
query2  = torch.randn(40, 1536)   # query in shape [batch, heads]
key     = torch.randn(50, 1536) # key in shape [batch, heads]
value   = torch.randn(7 * embed_dim)  # value in shape [batch, dim]
__output__  = m(query2, key, value)

