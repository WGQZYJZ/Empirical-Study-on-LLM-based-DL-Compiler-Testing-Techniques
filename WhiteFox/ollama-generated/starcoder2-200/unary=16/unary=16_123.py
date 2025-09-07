
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc  = torch.nn.Linear(784, 10)
 
    def forward(self, x1):
        v2  = self.fc(x1) 
        return relu(v2)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(64,784)
