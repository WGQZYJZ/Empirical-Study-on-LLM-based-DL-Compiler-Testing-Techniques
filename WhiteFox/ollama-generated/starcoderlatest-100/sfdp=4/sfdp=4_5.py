
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(512, 8)
        self.key = torch.nn.Linear(512, 8)
        self.value = torch.nn.Linear(512, 8)

    def forward(self, x1):
        v6 = self.query(x1)
        v7 = self.key(v6)
        v8 = self.value(v7)

        qk = v6 @ v7.transpose(-2, -1) / math.sqrt(v6.size(-1)) + attn_mask  # Compute the dot product of the query and key, and scale it
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result

        output = attn_weight @ v8  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 512, 64, 64)
