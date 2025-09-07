
class Model(torch.nn.Module):
    def __init__(self, n_heads, n_units, vocab_size, seq_length):
        super().__init__()
        self.encoder = TransformerEncoderLayer(n_units=n_units, n_heads=n_heads)
        self.linear = torch.nn.Linear(n_units, vocab_size)
 
    def forward(self, x):
        _ = self.encoder(x)
        v6  = self.linear(_).view(-1, _, _).permute(0, 2, 1) # view the last output to be the same shape as inputs
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
