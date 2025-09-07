
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(5, 2)
 
    def forward(self, x1):
        v1  = x1.view(-1, x1.shape[0], x1.shape[2] * x1.shape[3]) # Flatten the input
        v2  = self.fc(v1)                                       # Apply a fully connected layer to this tensor
        return torch.sigmoid(v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 5)
