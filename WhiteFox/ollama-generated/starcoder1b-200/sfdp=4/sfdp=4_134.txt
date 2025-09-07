
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(4, 8, dtype=torch.float))
        self.key    = torch.nn.Parameter(torch.randn(3, 64, 128, dtype=torch.float))
        self.value   = torch.nn.Parameter(torch.randn(3, 512, 768, dtype=torch.float))

    def forward(self, x1):
        v1 = x1 @ self.key.transpose(-2, -1) / math.sqrt(x1.size(-1)) # Compute the dot product of the query and key, and scale it
        v2 = v1 + self.attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(v2 @ self.value) # Apply softmax to the result

        out = attn_weight @ self.value
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
