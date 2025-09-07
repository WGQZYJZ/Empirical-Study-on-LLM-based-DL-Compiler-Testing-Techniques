
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(768, 128)
        self.key   = torch.nn.Linear(128, 128)
        self.value = torch.nn.Linear(128, 128)
        self.dropout = nn.Dropout()
        self.fc = torch.nn.Linear(128, 64)
 
    def forward(self, x):
        q = self.query(x).view(-1, x.size(1))
        k = self.key(x).view(-1, x.size(1))
        v = self.value(x).view(-1, x.size(1))
        out = torch.matmul(q, k)
        out = out + self.dropout((self.fc(x)))  # Use FFN to compute output
        return out


# Initializing the model
m = Model()


