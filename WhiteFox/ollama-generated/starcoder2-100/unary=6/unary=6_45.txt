
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3 # adding 3 to convolution result
        v2  = torch.clamp_min(v1, min=0)# clamping the addition operation of the convolution with min value set at 0
        v3  = torch.clamp_max(v2, max=6)# clamping the previous result with max value set at 6 
        v4  = v1 * v3 # multiplying the addition operation and the clamped result for ReLU6 activation function
        v5  = v4 / 6 # dividing the multiplication of the addition by 6
        return v5
 
# Initializing the model.
m  = Model()

