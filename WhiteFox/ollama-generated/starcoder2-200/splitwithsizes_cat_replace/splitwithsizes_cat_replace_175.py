
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
    def forward(self, x):
         #splitting and concatenation
         splitted_x = torch.split(x, 256, dim)
         concatenated_x = torch.cat([split for split in splitted_x], dim=0)
         return concatenated_x
 
 # Inputs to the model
 x  = torch.randn(8192, 3 ,4 )

 # Initializing the model
 m  = Model()

 # Initializing the input tensor: random tensor with size [batch, num_channel, height]
__output__  = m(x)