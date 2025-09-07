
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(2048, 1)
 
    def forward(self, x1):
        v1 = self.fc(x1)
        v2 = F.relu(v1)
        return v2


# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(10, 3 * 32 * 32).cuda()
__output__  = m(x1)