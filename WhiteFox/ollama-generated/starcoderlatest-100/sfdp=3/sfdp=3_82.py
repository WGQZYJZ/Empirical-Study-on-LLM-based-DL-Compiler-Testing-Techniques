
class Model(torch.nn.Module):
    def __init__(self, embed_dim=1024):
        super().__init__()
        self.layernorm1 = torch.nn.LayerNorm((64, 64))
        self.embed_tokens = torch.nn.Embedding(vocab_size, embed_dim)
 
    def forward(self, x):
        v  = self.layernorm1(x + F.embedding(input_tensor, self.embed_tokens))
        return v


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
