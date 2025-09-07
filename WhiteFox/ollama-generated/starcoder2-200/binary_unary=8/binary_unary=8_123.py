
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
 
        v2  = v1 + 5 # added tensor

        v3 = torch.relu(v2) # ReLU activation function
        return v3


# Initializing the model and inputs to it
m   = Model()
x1  = torch.randn(1, 3, 64, 64)
 
# Evaluating the output of the model on inputs x1
