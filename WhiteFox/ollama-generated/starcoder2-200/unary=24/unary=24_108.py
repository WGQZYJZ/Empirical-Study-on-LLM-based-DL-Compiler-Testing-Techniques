
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0 
        v3  = v1 * negative_slope # multiply the output of the convolution by a negative slope (default: -0.05). 
        v4  = torch.where(v2, v1, v3) # apply the where function to select elements from t1 or t3 based on mask t2
        return v4


# Initializing the model