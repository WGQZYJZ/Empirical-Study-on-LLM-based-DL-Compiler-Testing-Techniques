
class EncoderBlock(torch.nn.Module):
    def __init__(self, embed_dim=1024):
        super().__init__()
 
        self.norm  = torch.nn.LayerNorm([embed_dim])
        self.attn1 = torch.nn.MultiheadAttention(embed_dim, num_heads=8)
        self.attn2 = torch.nn.MultiheadAttention(embed_dim, num_heads=8)
 
    def forward(self, src):
        norm  = self.norm(src) # Apply the LayerNorm on the input tensor.
        attn1 = self.attn1(norm)[0] # Apply multi-head attention to the normalized input tensor.
        attn2 = self.attn2(attn1 + src)[0] # Add the original input with the output of the multihead attention and then apply another multiheaded attention operation on this tensor.

        return attn2


# Initializing the model
enc  = EncoderBlock()


# Input to the model