
class Model(torch.nn.Module):
    def __init__(self, n1, n2):
        super().__init__()
        self.linear = torch.nn.Linear(n1 + n2, 8)
 
    def forward(self, x1, x2):
        x1 = torch.cat([x1], dim=1)  # Add the input to a sequence of vectors with an additional axis of dimension `dim`.
        x2 = torch.cat([x2], dim=1)
        x3 = self.linear(torch.cat([x1, x2], dim=-1))  # Perform a matrix multiplication between `x1` and `x2`,
        # which is then added to the result of the previous step.
        return x3


# Inputs to the model
n1 = 8
n2 = 4
