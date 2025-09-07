
class Model(torch.nn.Module):
    def __init__(self, query_dim, key_dim, embed_dim=128):
        super().__init__()
 
        self.query_embed = torch.nn.Embedding(query_dim, embed_dim)
        self.key_embed   = torch.nn.Embedding(key_dim, embed_dim)
 
    def forward(self, query, key):
        # Please generate the inputs to be embedded in a 1D tensor.
        