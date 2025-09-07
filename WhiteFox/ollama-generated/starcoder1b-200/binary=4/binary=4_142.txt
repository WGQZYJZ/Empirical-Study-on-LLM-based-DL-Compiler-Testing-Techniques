
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 30)
 
    def forward(self, x):
        v = self.linear(x) + other # Add another tensor to the output of the linear transformation
        return v


# Initializing the model
m = Model()


