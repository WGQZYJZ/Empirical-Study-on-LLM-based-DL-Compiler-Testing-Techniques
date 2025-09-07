
class Model(torch.nn.Module):
    def __init__(self, d_k, nhead=8, dim_feedforward=2048):
        super().__init__()
        self.query = torch.nn.Linear(d_k, dim_feedforward)
        self.key = torch.nn.Linear(d_k, dim_feedforward)
        self.value = torch.nn.Linear(dim_feedforward, d_k)
 
    def forward(self, x1):
        qk  = self.query(x1).transpose(-2, -1) / math.sqrt(self.query.size(-1))
        qk  = qk + attention_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        value  = self.value(attn_weight @ x1)  # Compute the weighted sum of the value and attn_weights
        return value

# Initializing the model
m = Model(d_k=5)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
