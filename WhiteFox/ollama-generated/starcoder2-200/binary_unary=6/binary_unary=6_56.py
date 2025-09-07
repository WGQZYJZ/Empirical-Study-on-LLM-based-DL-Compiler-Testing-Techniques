
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(8, 32) # Apply a linear transformation with 8 input channels and 32 output channels to the input tensor
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 - other
        v3 = torch.relu(v2)
        return v3


# Initializing the model