
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(768, 128)
        self.linear2 = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        v1 = self.linear1(x1).view(-1, 768)
        v2 = F.relu(v1)
        v3 = self.linear2(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 512)
