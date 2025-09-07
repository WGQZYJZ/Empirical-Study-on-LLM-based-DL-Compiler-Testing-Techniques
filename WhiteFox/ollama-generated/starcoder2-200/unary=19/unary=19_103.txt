

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*384*384, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1) # Apply the sigmoid function to the output of the linear transformation
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 384*384*384) # Random input tensor with shape (batch_size, feature map size x feature map size x channel count) 
__output__  = m(x1)
