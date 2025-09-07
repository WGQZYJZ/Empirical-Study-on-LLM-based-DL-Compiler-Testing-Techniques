
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2): # The model has 3 inputs
        v1  = x1.permute(0, 2, 1) # Permute the first input tensor for 3D input
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v3  = x2 + v2
        return v3


# Initializing the model