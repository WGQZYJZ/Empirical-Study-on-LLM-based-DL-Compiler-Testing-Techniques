
class Model(torch.nn.Module):
    def __init__(self, dim_emb, dropout=0):
        super().__init__()
        self.dim_emb = dim_emb
        self.fc = torch.nn.Linear(dim_emb * 2, dim_emb)
 
    def forward(self, x1, x2):
        x = x1 + x2
        x = F.relu(self.fc(x))
        x = F.dropout(x, p=dropout, training=self.training)
        return x


# Initializing the model
m = Model(dim_emb=32)


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
