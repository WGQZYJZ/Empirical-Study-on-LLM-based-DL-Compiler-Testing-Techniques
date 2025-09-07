

class MyModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.norm1 = nn.LayerNorm(256)
        self.linear1 = nn.Linear(3, 4096)
        self.dropout1 = nn.Dropout(0.1)
        self.norm2 = nn.LayerNorm(256)
        self.linear2 = nn.Linear(7840, 100)


    def forward(self):
        x1 = self.norm1(x1) 
        x3 = self.dropout1(x1)
        x4 = torch.zeros(4,100)
        return self.linear2

