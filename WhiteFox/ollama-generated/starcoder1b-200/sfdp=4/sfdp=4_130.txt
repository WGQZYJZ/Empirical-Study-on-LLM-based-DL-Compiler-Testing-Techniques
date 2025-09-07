
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # Compute the dot product of the query and key tensors, and scale it
        qk = x1 @ x1.transpose(-2, -1) / math.sqrt(x1.size(-1)) + self._attn_mask
        # Apply softmax to the result
        attn_weight = torch.softmax(qk, dim=-1)
        # Compute the dot product of the attention weights and the value
        output = attn_weight @ x1  # (batch_size, seq_len, hidden_dim) * (seq_len, hidden_dim) -> (batch_size, hidden_dim)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
