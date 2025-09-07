
class EncoderBlock(nn.Module):
    def __init__(self, embedder):
        super().__init__()

        self.norm1  = nn.LayerNorm(embedder) # Apply layer normalization to the input
        self.attn   = nn.MultiheadAttention(embedder) # Define a multihead attention operation on the input using the embedded token size as head dimensionality
        self.norm2  = nn.LayerNorm(embedder) # Apply layer normalization to the output of the attention operation

    def forward(self, x1):

        y1 = self.norm1(x1) # Layer normalize the input tensor
        y2, attn_weight = self.attn(y1, y1, y1) # Apply multihead attention on the input with the input itself as both query and key inputs, and the output is also scaled by the square root of the embedded token size

        y3  = self.norm2(x2 + y1)
        return (y3), attn_weight

# Initializing the model