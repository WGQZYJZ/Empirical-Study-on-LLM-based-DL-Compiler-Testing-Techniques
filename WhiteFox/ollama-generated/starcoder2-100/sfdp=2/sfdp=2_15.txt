
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        conv_output  = self.conv(x1)
        
        conv2_output  = conv_output * 0.5

        conv3_output  = conv2_output + conv_output
        
        return conv3_output

# Initializing the model
m  = Model()


# Inputs to the model

x1  = torch.randn(1, 3, 64, 64)

__output__  = m(x1)
