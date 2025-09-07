
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() * self.negative_slope # Apply a boolean mask to the output of the linear transformation and multiply it by negative slope
        v3 = torch.where((v1 > 0).float(), v1, v2) # Apply Leaky ReLU on the output of the linear transformation where t1 is greater than zero if t2 is True, and then use the corresponding element from the output of the linear transformation where t1 is greater than zero if t3 is True
        return v3


# Initializing the model with negative slope=0.05
m = Model(negative_slope=0.05)

# Inputs to the model
x1 = torch.randn(4, 32, 64)
