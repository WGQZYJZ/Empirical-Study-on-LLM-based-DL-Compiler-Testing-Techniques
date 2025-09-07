
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=768, num_heads=12)
 
    def forward(self, x1):
        qk  = torch.matmul(x1, x1.transpose(-2,-1)) # Compute the dot product of x1 and itself
        qk  = qk.div(inv_scale_factor)         # Scale the dot product by an inverse scale factor
        qk  = self.attn(qk, x1, x1)[0]          # Apply multihead attention with dimension = [query length, key length, head dim]
        dropout_qk  = torch.nn.functional.dropout(qk, p=dropout_p)
        output  = self.mha(dropout_qk, x1, x1)   # Apply mha
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 768, 3000, 400)
