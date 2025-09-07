
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=64, num_heads=8)
 
    def forward(self, x1, x2):
        # Multihead attention with 8 heads and a size of query embedding (x1) and key embedding (x2). The input
        # should be the output of the convolutional layer. Output shape is batch-size = 1, sequence length = 4, 
        # and embed_dim = 64. You can learn more about MultiheadAttention() in PyTorch's documentation: 
        # https://pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html
        attn, _ = self.attention(x1, x2)
        return attn

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
