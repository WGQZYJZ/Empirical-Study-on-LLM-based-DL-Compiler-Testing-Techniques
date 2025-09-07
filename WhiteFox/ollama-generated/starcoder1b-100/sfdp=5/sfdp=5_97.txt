
class Model(torch.nn.Module):
    def __init__(self, hidden_dim=256, attn_layer=1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(hidden_dim, attn_layer)

    def forward(self, x, k, v):
        x  = self.attn(x, k, v)  # Compute the attention output
#        return value  # Return the final output


# Initializing the model
m = Model()

