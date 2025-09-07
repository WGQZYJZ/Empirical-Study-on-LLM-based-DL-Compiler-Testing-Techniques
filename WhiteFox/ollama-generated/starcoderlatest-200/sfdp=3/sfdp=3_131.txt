
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim, num_heads=8)
 
    def forward(self, query, key, value, scale_factor, dropout_p):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
query  = torch.randn(1, 3, embed_dim, num_heads) # input: (batch_size, nhead, q, kv)
key    = torch.randn(1, 8, embed_dim, num_heads) # input: (batch_size, nhead, q, kv)
value  = torch.randn(1, 8, embed_dim, num_heads) # input: (batch_size, nhead, k, v)
scale_factor  = 0.75
dropout_p     = 0.4
__output__    = m(query, key, value, scale_factor, dropout_p)


