
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor 
        v2  = v1 * 0.5 # Multiply the output of the convolution by 0.5
        v3  = torch.where(v2>0, v2*v2, -v2-1) # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 64, 64) # Input tensor of shape (batch_size x number_of_channels x height x width). 
__output__  = m(x1)