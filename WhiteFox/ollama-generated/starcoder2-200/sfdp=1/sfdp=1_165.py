
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
         v1  = self.conv(x1)
         v2  = torch.matmul(v1,v1.transpose(-2,-1))
         return v2
# Initializing the model
m = Model()
 
# Inputs to the model
x1=torch.randn(8,3,4,5)# x1 is the input tensor of shape (batch_size X number_of_channels, number_of_input_width,  number_of_input_height)
