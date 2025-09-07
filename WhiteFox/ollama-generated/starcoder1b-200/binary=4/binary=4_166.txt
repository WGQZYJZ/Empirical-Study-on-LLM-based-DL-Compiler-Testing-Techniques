
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 3)
 
    def forward(self, x1):
        return self.linear(x1 + 2)  # Add another input tensor to the output of the linear transformation


# Initializing the model
m = Model()


