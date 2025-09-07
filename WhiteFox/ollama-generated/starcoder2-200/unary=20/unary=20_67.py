
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.sigmoid(x1) # Apply the sigmoid function to each element of x1
        return v2

