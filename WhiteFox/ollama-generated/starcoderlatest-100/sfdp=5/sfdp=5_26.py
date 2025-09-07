
class AttentionModel(torch.nn.Module):
    def __init__(self, num_heads=8, dim_feedforward=2048):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv_out = torch.nn.Linear(in_features=64 * num_heads, out_features=dim_feedforward)
        self.dropout = torch.nn.Dropout(p=0.5)
        self.layer_norm = torch.nn.LayerNorm([64 * num_heads], eps=1e-7)

    def forward(self, x):
        v1  = self.conv(x)

        qk = torch.einsum('b i j k, b l m n -> (b i j) (b l n)', v1, v1) / math.sqrt(v1.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_mask = torch.triu(torch.ones((64 * 8, 64 * 8)), diagonal=1).view([64, 64])
        qk = qk + attn_mask

        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True) # Apply dropout to the softmax output
        
        output = attn_weight @ v1  # Compute the dot product of the dropout output and the value

        return output

# Initializing the model
m = AttentionModel()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
