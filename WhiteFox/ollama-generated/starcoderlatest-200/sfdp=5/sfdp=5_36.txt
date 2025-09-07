
class MultiHeadSelfAttention(torch.nn.Module):
    def __init__(self, embedding_dim, num_heads=8):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_heads = num_heads
        # Please fill out the code to construct self-attention layer.

    def forward(self, x1, x2):
        __output__  = attn_weight @ value  # Compute the dot product of the dropout output and the value
        return attn_weights


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = MultiHeadSelfAttention(128)
 
    def forward(self, x1, x2):
        v1  = self.attention_layer(x1, x2) # Apply the self-attention layer with input from query and key.
        return v1
