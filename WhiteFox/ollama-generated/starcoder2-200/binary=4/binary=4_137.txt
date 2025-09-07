
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying the linear transformation to an input tensor
        v2  = v1 + torch.zeros((v1.shape[0], ))  # Adding another constant to the output of the linear transformation
        return v2

# Initializing the model