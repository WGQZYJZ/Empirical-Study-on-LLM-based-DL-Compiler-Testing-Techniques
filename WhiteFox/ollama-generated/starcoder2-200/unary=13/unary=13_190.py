
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.linear = torch.nn.Linear(576*4*4,2048)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 1 # Just for demonstration purposes. The actual model may contain more operations.
        v3 = self.linear(v2)
 
        # This is a valid linear-sigmoid model, because the input tensor 
        # that will be passed to the sigmoid function contains the result of the first 
        # operation (the addition), which is 1. So it does not matter what the 
        # input tensor actually is in this example.
        v4 = torch.sigmoid(v3)
 
        return v2 * v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(5, 8*4*4)
__output__  = m(x1)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -