
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=768):
        super().__init__()

        self.embedding = torch.nn.Embedding(num_embeddings=30522, embedding_dim=embedding_dim)
        self.norm  = torch.nn.LayerNorm(normalized_shape=[-1])
        self.transformer = torch.nn.TransformerEncoder(
            torch.nn.TransformerEncoderLayer(d_model=768, nhead=12), num_layers=4, norm=self.norm)

    def forward(self, input): 
        v  = self.embedding(input).transpose(-3,-2)
        v  = self.transformer(v)
        return v.permute(-2,-1)[0][-1]


# Initializing the model
m  = Model()

 # Inputs to the model
input = torch.randint_like([256, 768], dtype=torch.int32, low=0, high=30522)
 