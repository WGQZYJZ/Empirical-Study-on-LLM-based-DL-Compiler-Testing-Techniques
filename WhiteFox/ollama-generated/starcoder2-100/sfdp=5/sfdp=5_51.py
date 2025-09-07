
class Model(torch.nn.Module):
    def __init__(self, nhead=8, dropout=0.5):
        super().__init__()
        self.linear = torch.nn.Linear(32768, 4)
        self.transformer = torch.nn.TransformerEncoderLayer(d_model=1024, nhead=nhead, dim_feedforward=32 * 8, dropout=dropout)
 
    def forward(self, src):
        v1 = self.linear(src)
        v2 = v1 @ v1.transpose(-2, -1) / math.sqrt(v1.size(-1)) + torch.nn.MaskedMultiheadAttention()(v1, v1, v1) # Compute the dot product of the query and key, and scale it 
        attn_mask = torch.full([50], float("-inf"), device=src.device).unsqueeze(dim=-2)
        attn_weight  = F.softmax(v2 + attn_mask, dim=-1) # Apply softmax to the result 
        attn_weight = dropout(attn_weight, p=dropout, training=self.training)  # Apply dropout to the softmax output 
        return v2 @ v2

# Initializing the model
m = Model()
 
# Input tensor for the model 
x1 = torch.randn(4, 3, 60)


# Inputs to the model
x1 = torch.randn(4, 3, 50) # The dimension of the input tensor must be different from that of the previous input.