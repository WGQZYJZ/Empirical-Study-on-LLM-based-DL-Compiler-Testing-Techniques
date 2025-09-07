
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=300):
        super().__init__()
        self.embedding = torch.nn.Embedding(128, embedding_dim)
        self.layer_norm = torch.nn.LayerNorm(embedding_dim)
 
    def forward(self, x1):
        v1 = self.embedding(x1).reshape(-1, 1, 64, 64)
        v2 = self.layer_norm(v1).transpose(1, 2).contiguous().view(1, -1)
        v3 = torch.matmul(v1, v2).squeeze(-1)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 128, 64, 64)
