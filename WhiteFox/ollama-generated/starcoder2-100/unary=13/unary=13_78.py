
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 4)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
torch.manual_seed(1053)  # For consistency in testing across environments, please set this seed for reproducibility (you may find it helpful if you want to re-run your analysis).
x1 = torch.randn(28674, 128)

# Calculating output from the model using forward pass
