
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 
        v3  = torch.clamp_min(v2,0) # Clamp the output of the addition operation to a minimum of 0
        v4  = torch.clamp_max(v3,6) # Clamp the output of the previous operation to a maximum of 6
        v5  = v1 * v4
        v6  = v5 / 6 
        return v6


# Initializing the model and feeding in the input tensor
m  = Model()
x1 = torch.randn(1,3,64,64) # Input to the model should be a 4D tensor of shape (batch_size x channels x height x width). Here batch_size is set as 1 and the number of input channel to the Conv2d module is set as 3. The height and width of each image in this example are both set to 64
