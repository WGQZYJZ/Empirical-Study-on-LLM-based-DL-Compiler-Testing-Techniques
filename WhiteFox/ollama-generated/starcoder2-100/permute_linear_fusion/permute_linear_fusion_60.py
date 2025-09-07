
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1.permute(0, 2) # swaps the 2nd and 3rd dimension of this tensor.
        v2 = torch.nn.functional.linear(v1, self.linear_layer())
        return v2

    def linear_layer():
    return torch.nn.Linear(in_features=2, out_features=2)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 2)

 