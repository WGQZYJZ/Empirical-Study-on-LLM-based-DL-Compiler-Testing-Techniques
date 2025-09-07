
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.linear2 = torch.nn.Linear(8, 4)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = v1 * 0.5
        v3 = torch.sqrt(torch.sum(v2**2, dim=1)) + 1 # Sum of squared output
        v4 = torch.exp(torch.log(v3) - v2)
        v5 = torch.sum(v4 ** 2) * 0.044715  # Product of output of linear transformation with itself multiplied by `0.044715`
        v6 = v3 + v5  # Output of linear transformation cubed plus output of previous operation
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
