
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 3, 2).reshape(-1, 4) # Permute the input tensor. In this example, we swap dimensions (0, 3), and then reshape it to have a new shape (-1, 4).
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) 
        return v2


# Initializing the model
m = Model()


# Inputs to the model