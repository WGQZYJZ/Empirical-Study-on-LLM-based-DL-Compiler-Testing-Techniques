
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self._other_tensor  = torch.randn((640))
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self._other_tensor
        v3  = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1, 3, 640 , 640 )
 
__output__  = m(x1)

