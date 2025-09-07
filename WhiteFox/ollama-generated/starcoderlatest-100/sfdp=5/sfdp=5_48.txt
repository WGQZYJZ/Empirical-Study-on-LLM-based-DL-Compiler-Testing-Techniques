
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 64)
        self.key = torch.nn.Linear(1024, 64)

    def forward(self, x1, x2):
        qk = self.query(x1) @ self.key(x2).transpose(-2, -1) / math.sqrt(1024) + attn_mask
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(50, 64, 384, 256)
x2 = torch.randn(50, 64, 256, 128)
