
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(in_features, out_features, bias=True)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # The result of the linear transformation is then add to 'other' 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, in_features, device=device)
