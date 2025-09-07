
class Model(torch.nn.Module):
    def __init__(self, other=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Add the input tensor and another to the output of the linear transformation
        return v1


# Initializing the model
m = Model()


