

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.15329874643916567)
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1):
        v1  = self.conv(x1)

        v2  = (v1 > 0).to(torch.float64) # The .to() function is used to convert the data type of a tensor. In this case, it converts the output of the comparison operation between the convolutional layer and zero from bool to float64
        v3  = v2 * negative_slope

        v4 = torch.where(v1 > 0., v1, v3)
        
        return v4


# Initializing model