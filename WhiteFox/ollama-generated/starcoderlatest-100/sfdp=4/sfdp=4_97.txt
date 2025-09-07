
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        # Compute the dot product of the query and key, and scale it
        # The first dimension is the batch size (number of queries)
        qk  = torch.einsum('b i d, b j d -> b i j', q1, k1) / math.sqrt(q1.size(-1))
        # Add the attention mask to the scaled dot product
        qk  = qk + attn_mask
        # Apply softmax to the result and the shape of `qk` remains unchanged
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v1
        return output

# Initializing the model
m = Model()


# Inputs to the model
q1  = torch.randn(32, 48, 64, 64)
k1  = torch.randn(32, 96, 64, 64)
v1  = torch.randn(32, 96, 64, 64)


