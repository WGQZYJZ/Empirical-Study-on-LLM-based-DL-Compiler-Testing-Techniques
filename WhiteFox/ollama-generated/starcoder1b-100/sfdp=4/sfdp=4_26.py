
class Model(torch.nn.Module):
    def __init__(self, query_layer, key_layer, attn_layer):
        super().__init__()
        self.query = torch.nn.Linear(query_layer.in_features, key_layer.out_features)
        self.key = torch.nn.Linear(key_layer.in_features, key_layer.out_features)
        self.attn = attn_layer
        self.v = torch.nn.Linear(key_layer.out_features, query_layer.in_features)
 
    def forward(self, x1, x2):
        # Query: 1045920x384 -> 384x384x64
        # Key: 384x64 -> 64x64x128
        q = self.query(x1).view(-1, 1, x1.size(1), x1.size(2))
        k = self.key(x2)
        attn = self.attn(q, k, key_padding_mask=torch.eye(x2.shape[-1]).bool())  # Query: 384x64 -> 64x64x64
        v = attn @ self.v(k).view(-1, k.size(-1))
        return self.v(v)


# Inputs to the model
query_layer  = torch.randn(1045920, 384)
key_layer  = torch.randn(384, 64)
attn_layer  = nn.Softmax(dim=-1)
__output__  = Model(query_layer, key_layer, attn_layer)(x1, x2)


