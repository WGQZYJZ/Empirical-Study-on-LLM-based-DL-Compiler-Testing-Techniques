
class Model(torch.nn.Module):
    def __init__(self, nhead=4):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(3072, nhead)
 
    def forward(self, query: Tensor, key: Optional[Tensor] = None, value: Optional[Tensor] = None, attn_mask: Optional[Tensor] = None):
        return self.attn(query, key=key, value=value, attn_mask=attn_mask)[0]


# Initializing the model with 3 attention heads each.
m = Model(nhead=3)

# Inputs to the model. 
x1 = torch.randn(24, 8, 96, 96)
x2 = torch.randn(20736, 1024).permute(0, 2, 1) # Attention mask. It is a tensor of shape (batch_size, seq_length), where all values are zeros and one value at index 8 is assigned the value 1. This value should be equal to 1 for positions where attention will not be applied. 
