
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 2)
        self.linear2 = torch.nn.Linear(4, 5)

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear1.weight, self.linear1.bias) # Apply linear transformation to the input tensor.
        v2 = v1.permute(-2, -1).view(-1, 5 * 2) # Permute and reshape output of the linear transformation.
        v3 = torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias) 
        return v3


# Initializing the model