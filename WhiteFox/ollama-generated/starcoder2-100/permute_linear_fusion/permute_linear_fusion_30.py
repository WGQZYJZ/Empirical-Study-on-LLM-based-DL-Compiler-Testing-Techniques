
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x1):
        v1 = x1.permute(1, 0).reshape(-1, 5 * 3) # Permute and reshape the input tensor to a flat representation
        v2 = self.linear(v1)                       # Apply linear transformation on the permuted and reshaped flattened tensor
        return v2


# Initializing model
m = Model()
