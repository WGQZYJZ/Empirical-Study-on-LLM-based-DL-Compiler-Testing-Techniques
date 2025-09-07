
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(1024, 512)
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, x):
        v1 = F.relu(self.linear1(x))
        v2 = self.dropout(v1)
        return v2
# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(4, 3, 64, 64)
