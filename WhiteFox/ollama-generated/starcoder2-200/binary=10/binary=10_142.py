
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 10)
 
    def forward(self, x2):
        v2 = self.linear(x2 + other) # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model