
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model
m = Model()

