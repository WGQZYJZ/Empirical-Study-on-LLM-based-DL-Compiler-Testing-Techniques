
class Model(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.fc1 = nn.Linear(embed_dim, embed_dim)
        self.dropout = nn.Dropout(0.5)
 
    def forward(self, x1):
        v = self.fc1(x1)  # Linear transformation to the input data
        return v + self.dropout(v)


# Initializing the model
m = Model(embed_dim=embed_dim)


