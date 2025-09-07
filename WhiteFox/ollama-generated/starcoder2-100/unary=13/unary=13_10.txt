
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 8, 16)
 
    def forward(self, x1):
        v0  = F.sigmoid(self.linear(x)) # Apply the sigmoid function to the output of a linear transformation on the input tensor
        v1  = self.linear(v0) 
        return v2


# Initializing the model