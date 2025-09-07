
class TransformerModel(torch.nn.Module):
    def __init__(self, n_head=16):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.layer_norm1 = nn.LayerNorm(8, elementwise_affine=False)
        self.ffn_actv = F.gelu
        # The number of heads is the same as that in the BERT paper.
        self.attention_heads = n_head
        self.multihead_attn = MultiHeadAttention()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        attn_output  = self.multihead_attn(v1, None, None) # Apply multi-head attention to the output of convolution layer.
        v2  = v1 + attn_output
        v2 = self.layer_norm1(v2)
        return self.ffn_actv(v2)


# Initializing the model
m = TransformerModel()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
