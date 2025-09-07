
class Model(torch.nn.Module):
    def __init__(self, embedding_size=16, hidden_size=128, num_heads=8, ff_hidden_size=256):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embedding_size, num_heads)
        self.ff = torch.nn.Sequential(
            torch.nn.Linear(embedding_size + hidden_size * 2, ff_hidden_size),
            torch.nn.ReLU(),
            torch.nn.Dropout(dropout_p),
            torch.nn.Linear(ff_hidden_size, embedding_size)
        )
 
    def forward(self, x1, x2):
        v = self.attention(x1, x2)[0]  # Apply multihead attention to the query and key
        output = self.ff(torch.cat([v, x1, x2], dim=1))  # Compute the dot product of these attention weights with the inputs
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
