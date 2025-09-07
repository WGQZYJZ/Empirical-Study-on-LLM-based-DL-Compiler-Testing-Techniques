
class Model(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.qkv = torch.nn.Linear(embed_dim * 3, embed_dim)
 
    def forward(self, x1):
        v1 = x1.view(-1, 240)
        w1, b1 = self.qkv(v1).split([embed_dim], dim=-1)
        w1 = F.gelu(w1) + b1
        w1 = torch.nn.functional.dropout(w1, p=dropout_p)
        v2 = x1.view(-1, 360)
        w2, b2 = self.qkv(v2).split([embed_dim], dim=-1)
        w2 = F.gelu(w2) + b2
        w2 = torch.nn.functional.dropout(w2, p=dropout_p)
        v3 = x1.view(-1, 480)
        w3, b3 = self.qkv(v3).split([embed_dim], dim=-1)
        w3 = F.gelu(w3) + b3
        w3 = torch.nn.functional.dropout(w3, p=dropout_p)
        output = w1 * w2 + w3 
        return output

 # Initializing the model
m = Model(embed_dim)
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
