
class Model(torch.nn.Module):
    def __init__(self, min_value=-10.0, max_value=10.0):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=32 * 64 * 64, out_features=8)
        self.clamp = torch.nn.Clamp(min_value=-10.0, max_value=10.0)
 
    def forward(self, x1):
        v1 = self.linear(x1).clamp(min_value=-10.0, max_value=10.0)  # Apply a linear transformation to the input tensor
        return v1


# Initializing the model
m = Model()


