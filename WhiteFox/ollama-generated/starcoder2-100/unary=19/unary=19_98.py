
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 8 * 49, 1)

    def forward(self, x):
        v1 = self.linear(x) 
        v2 = torch.sigmoid(v1) # Apply sigmoid function to output of linear transformation
        return v2

# Initializing the model
m = Model()

