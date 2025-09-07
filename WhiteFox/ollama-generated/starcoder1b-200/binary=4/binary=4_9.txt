
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.linear1(x1) + other  # Apply a linear transformation to the input tensor
        v2 = v1 * 0.5              # Multiply the output of the linear transformation by 0.5
        return v2


# Initializing the model
m = Model()


