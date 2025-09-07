
class Model(torch.nn.Module):
    def __init__(self, d_model=256):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=d_model,  # Embedding size of each token (number of features for the model)
            num_heads=4,  # Number of attention heads to use in the MultiheadAttention layer
            dropout=0.1,
        )
 
    def forward(self, x1, x2):
        qk = self.attn(x1, x2)[0]
        return qk


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 4, 32, 32)
