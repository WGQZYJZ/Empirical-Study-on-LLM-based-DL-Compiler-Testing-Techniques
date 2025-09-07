
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3 * 64 * 64, 2)
 
    def forward(self, x1):
        v1  = self.fc(x1.view(-1, 3*64*64))
        v2  = torch.sigmoid(v1)
        return v2
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
