
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
        # Note: The number of features in the input tensor must match that 
        # in the model definition above
    
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor
        return v2


# Initializing the model