
class Model(torch.nn.Module):
    def __init__(self, embed_dim=768, hidden_dim=3072, num_layers=12):
        super().__init__()
        self.linear = torch.nn.Linear(embed_dim, hidden_dim)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1
 
model  = Model()
x1 = torch.randn(2048, embed_dim=768)
__output__  = model(x1)

