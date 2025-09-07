
class Model(torch.nn.Module):
    def __init__(self, vocab_size, embedding_dim):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embedding_dim)
        self.conv = torch.nn.Conv2d(16, 32, 4, stride=2, padding=1)
 
    def forward(self, x):
        e = self.embedding(x)
        return self.conv(e).flatten()

# Initializing the model
m = Model(vocab_size=50, embedding_dim=8)

# Inputs to the model
inputs  = [torch.randn(16), torch.randn(32)]
