
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(
            embed_dim=128, num_heads=16, dropout=0.25)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        return self.multihead_attention(query, key, value,
                                         attn_mask=None)[0]


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 128, 512, 8) # query of shape (B, H, N, L)
key   = torch.randn( 8, 128, 512, 8) # key of shape (D, H, M, L)
value = torch.randn( 8, 128, 512, 8) # value of shape (D, H, N, L)
