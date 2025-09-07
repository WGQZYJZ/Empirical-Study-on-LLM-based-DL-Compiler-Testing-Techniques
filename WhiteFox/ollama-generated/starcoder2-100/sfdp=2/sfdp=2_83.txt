
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(2, 3)
 
    def forward(self, x):
        v1 = self.linear1(x) # Apply a linear layer with 2 neurons to the input tensor
        v2 = v1 ** 2 + 10  # Compute v1 to the power of two and then add 10
        return v2


# Initializing model