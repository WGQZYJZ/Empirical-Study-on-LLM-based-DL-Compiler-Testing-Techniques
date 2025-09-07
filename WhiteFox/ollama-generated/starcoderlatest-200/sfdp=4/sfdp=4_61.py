
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 64)
        self.key = torch.nn.Linear(128, 64)

    def forward(self, x):
        qk = self.query @ self.key.transpose(-2, -1) / math.sqrt(128 * 3 * 5 * 5) # Compute the dot product of the query and key, and scale it
        return qk


# Initializing the model
attn = Attention()

# Inputs to the model
x = torch.randn(4, 64, 128, 5, 5)
