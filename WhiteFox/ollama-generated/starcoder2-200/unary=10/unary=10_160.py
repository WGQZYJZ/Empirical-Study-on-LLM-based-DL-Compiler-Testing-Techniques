
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + 3
        v3 = F.relu6(v2)
        v4 = v3 / 6
        return v4

# Initializing the model
m = Model()

 # Inputs to the model
input_data  = torch.randn(64, 784)
 
 