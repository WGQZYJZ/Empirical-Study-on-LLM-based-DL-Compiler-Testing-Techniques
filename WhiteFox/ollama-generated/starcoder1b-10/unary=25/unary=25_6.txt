
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8, bias=False)
 
    def forward(self, x1):
        return self.linear(x1) * -0.7071067811865476 # Apply the linear transformation to the input tensor and then multiply it by a negative slope


# Initializing the model
m = Model()

