
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        v2 = F.relu(v1) # The ReLU activation function is used in this model.
        return v2


# Initializing the model