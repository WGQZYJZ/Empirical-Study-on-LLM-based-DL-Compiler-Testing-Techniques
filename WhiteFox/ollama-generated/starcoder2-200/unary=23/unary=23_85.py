
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.convTrans(x1)  # The definition of the convTrans convolutional transpose
        return torch.tanh(v2)


# Initializing the model