
class Model(torch.nn.Module):
    def __init__(self, embed_dim=32):
        super().__init__()
        self.embed = torch.nn.Embedding(max_length, embed_dim)

    def forward(self, x1, x2):
        v1  = self.embed(x1)
        v2 = x2 + 1
        v3 = v1 * v2
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
input_tensor = torch.randn(1, max_length, embed_dim=embed_dim)
x1 = torch.randint(0, embed_dim, (max_length,))
x2 = torch.randint(0, embed_dim, (max_length,))
