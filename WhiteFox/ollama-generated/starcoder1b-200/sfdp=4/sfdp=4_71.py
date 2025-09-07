
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key = torch.nn.Linear(3, 16)
        self.value = torch.nn.Linear(32, 32)
        self.attn = torch.nn.Softmax(dim=-1)

    def forward(self, x):
        qk  = self.query(x).transpose(-2, -1) / math.sqrt(x.size(-1))  # Compute the dot product of the query and key, and scale it
        attn_mask = torch.ones(qk.shape[0], qk.shape[1], dtype=torch.bool)  # Add attention mask to the scaled dot product
        attn_weight  = self.attn(qk * attn_mask)  # Apply softmax to the result
        value = self.value(x).transpose(-2, -1)  # Compute the dot product of the attention weights and the value
        return attn_weight @ value


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
