
class Model(torch.nn.Module):
    def __init__(self, embed_dim=768):
        super().__init__()
        self.embed  = torch.nn.Embedding(30522, embed_dim)
        self.lnorm  = torch.nn.LayerNorm(embed_dim, eps=1e-05)
 
    def forward(self, input_ids):
        v4  = self.embed(input_ids).permute((0, 3, 1, 2)).contiguous()
        v5  = self.lnorm(v4)
        return v5

# Initializing the model
m  = Model(768)

 # Inputs to the model
input_ids = torch.randint(low=0, high=30522-1, size=(24,))
