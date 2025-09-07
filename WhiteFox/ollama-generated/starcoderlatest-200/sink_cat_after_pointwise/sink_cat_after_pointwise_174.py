
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 8)

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=1)  # Concatenate the two input tensors along dim=1
        v1 = t1.view(-1, 4)           # Reshape and view the concatenated tensor as (-1, 4). The -1 is not required in some cases. This method does not reshape tensor but creates a view of it. 
        v2 = self.relu(v1)          # Apply ReLU to the reshaped and permuted tensor
        return torch.nn.functional.linear(v2, self.linear1.weight, self.linear1.bias), \
               torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias)

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 2, 2)
__output__, 