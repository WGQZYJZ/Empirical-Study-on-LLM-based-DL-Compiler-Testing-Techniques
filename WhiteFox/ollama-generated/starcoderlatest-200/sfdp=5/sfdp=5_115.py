
class TransformerLayer(torch.nn.Module):
    def __init__(self, embed_dim=512, num_heads=8):
        super().__init__()

        # Multi-head Attention (MHA)
        self.attn = MultiHeadAttention(embed_dim, num_heads)
 
        # Feedforward Layer
        self.feed_forward = FeedForwardLayer(embed_dim)
 
    def forward(self, x1):
        attn_output = self.attn(x1)  # Multi-head attention computation
        ffn_output = self.feed_forward(attn_output)  # Feedforward computation
 
        return ffn_output
 
class Model(torch.nn.Module):
    def __init__(self, transformer_blocks=2):
        super().__init__()
        for _ in range(transformer_blocks):
            self.add_module("TransformerLayer", TransformerLayer())
 
    def forward(self, x1):
 
        return x1
 
