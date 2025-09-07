
class Model(torch.nn.Module):
    def __init__(self, qkv_size=512, embed_dim=768, depth=12, heads=8):
        super().__init__()
        self.layers = torch.nn.ModuleList([
            EncoderLayer(qkv_size, embed_dim, head) for _ in range(depth)])
 
    def forward(self, x1, x2):
        y1 = x1
        # Each layer of the transformer is composed by a sublayer, so y1 is a list.
        for i, (layer) in enumerate(self.layers):
            yi  = layer(y1)
            if i < depth - 1:
                y1  = torch.cat([y1, yi], dim=1)
        return y1


# Initializing the model
m = Model()


