
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(64 * 64, 1)
 
    def forward(self, x1):
        v1 = self.fc(x1.view(-1)) # Flatten the input tensor before applying linear transformation and non-linear activation function
        v2 = torch.nn.functional.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
