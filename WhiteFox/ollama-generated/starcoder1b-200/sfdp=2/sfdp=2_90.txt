
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=256, depth=4, heads=8):
        super().__init__()
        self.positionwise_feed_forward = PositionwiseFeedForward(hidden_dim=hidden_dim, depth=depth, heads=heads)
        self.layernorm = torch.nn.LayerNorm(self.hidden_dim)

    def forward(self, x1, x2):
        hidden = self.positionwise_feed_forward(x1)
        hidden = self.layernorm(x1 + hidden)
        return x1 + hidden


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
