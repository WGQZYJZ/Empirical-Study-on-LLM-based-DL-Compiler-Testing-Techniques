
class Model(torch.nn.Module):
    def __init__(self, qk_scale=None, attn_dropout=0.1, proj_dropout=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.proj = torch.nn.Linear(8 * 5 * 5, 8 * 5 * 5)
 
    def forward(self, x1):
        x1 = self.conv(x1)
        batch_size, seq_len, num_features = x1.shape
        x1 = x1.view(batch_size, -1, num_features)
        qk = x1 @ x1.transpose(-2, -1) / math.sqrt(num_features)  # Compute the dot product of the query and key, and scale it
        attn_mask = torch.triu(torch.ones((batch_size, seq_len, seq_len)))
        qk = attn_mask @ qk + 1e-12 * (torch.eye(seq_len) - 1) # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        attn_weight = torch.dropout(attn_weight, dropout_p, True)  # Apply dropout to the softmax output
        x2 = attn_weight @ x1
        return self.proj(x2)


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
