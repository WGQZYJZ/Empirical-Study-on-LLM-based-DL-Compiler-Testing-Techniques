
class Model(torch.nn.Module):
    def __init__(self, embed_dim=512):
        super().__init__()
        self.embedding = torch.nn.Embedding(vocab_size, embed_dim)

    def forward(self, input):
        emb = self.embedding(input[:, 0])
        return emb


# Initializing the model
m = Model()


