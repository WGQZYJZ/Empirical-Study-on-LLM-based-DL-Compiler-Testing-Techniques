
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(4096, 2048)
        self.dropout = torch.nn.Dropout(p=0.3)
        self.linear2 = torch.nn.Linear(2048, 512)
 
    def forward(self, x):
        x1 = self.linear1(x)
        x2 = F.relu_(self.dropout(x1))
        x3 = self.linear2(x2)
        return x3


# Initializing the model
m = Model()
# Inputs to the model
