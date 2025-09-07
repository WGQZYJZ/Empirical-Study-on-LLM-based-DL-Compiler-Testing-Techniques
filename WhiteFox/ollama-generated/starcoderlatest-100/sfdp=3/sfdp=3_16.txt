
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, num_heads, dropout=0):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout)
        self.kconv = torch.nn.Conv2d(3, d_model * 4, 1, stride=1, padding=1)

    def forward(self, query, key, value):
        # Concatenate the query tensor and the key tensor
        x = torch.cat([query, key, value], dim=1)
        qk = self.kconv(x)
 
        # Reshape the result of the dot product so that it can be processed by an attention head
        qk_reshaped = qk.permute(0, 2, 3, 1).contiguous().view(query.size(0), query.size(1), -1, num_heads)
 
        # Compute the attention on the attention heads and concatenate them to form a single tensor
        attn = self.dropout(qk_reshaped)
        output = torch.matmul(attn, value.transpose(-2, -1)).permute(0, 3, 1, 2).contiguous().view(query.size(0), num_heads * d_model, query.size(2), query.size(3))
 
        # Dropout the attention head results
        return output


# Initializing the model
m = MultiHeadAttention(512, 8)

# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
query = x1[:, :3]
key = x1[:, 3:6]
value = x1[:, 6:9]
