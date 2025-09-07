
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 6)
        self.linear2 = torch.nn.Linear(6, 6)
        self.dropout1 = torch.nn.Dropout(p=0.4)
        self.dropout2 = torch.nn.Dropout(p=0.2)
 
    def forward(self, x1):
        h1 = self.linear1(x1)
        h1 = F.gelu(h1)
        h2 = self.linear2(h1)
        h2 = self.dropout1(h2)
        output = self.linear2(self.dropout2(h2))
        return output


# Initializing the model
m  = Model()
x1 = torch.randn(2, 3, 64, 64)
