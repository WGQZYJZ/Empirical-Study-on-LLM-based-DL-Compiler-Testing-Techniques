
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.sigmoid(self.linear(x))  # Applying the sigmoid function to the output of the linear transformation
        return v
 
 
