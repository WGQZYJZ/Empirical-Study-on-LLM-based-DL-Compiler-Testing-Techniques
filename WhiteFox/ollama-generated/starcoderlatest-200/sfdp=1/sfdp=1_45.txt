
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(512, 1024)
        self.dropout1 = torch.nn.Dropout(0.3)
        self.linear2 = torch.nn.Linear(1024, 512)
        self.dropout2 = torch.nn.Dropout(0.3)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = F.relu(v1)
        v3 = self.dropout1(v2)
        v4 = self.linear2(v3)
        v5 = F.relu(v4)
        v6 = self.dropout2(v5)
        return v6


# Initializing the model
m = Model()

 # Inputs to the model
x  = torch.randn(8, 512, 7, 7)
