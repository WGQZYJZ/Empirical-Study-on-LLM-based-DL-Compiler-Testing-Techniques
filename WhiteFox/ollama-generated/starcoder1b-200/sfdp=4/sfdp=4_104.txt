
class Model(torch.nn.Module):
    def __init__(self, d_model, nhead):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_model, nhead)
        self.linear1 = torch.nn.Linear(d_model, 4 * d_model)
        self.fc1 = nn.Linear(4 * d_model, 256)
        self.fc2 = nn.Linear(256, 10)
 
    def forward(self, x1):
        b, s, c = x1.shape
        q = self.attn(x1, x1, x1)[0] # Compute the dot product of each item in the batch, and scale it
        # Multiply the result with the weights (softmax of scaled dot product of query and key),
        # Then apply a residual connection
        q_proj = torch.einsum('bsij,bj->bijs', q, x1) * attn_mask
        # Now compute the linear projection part
        v = self.linear1(q_proj)  # shape [batch_size, 2*hidden_dim]
        v = torch.cat([v, x1], dim=-1)
        v = F.gelu(self.fc1(v))
        logits = self.fc2(F.relu(v))
        return logits


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 500, 64, 64)
