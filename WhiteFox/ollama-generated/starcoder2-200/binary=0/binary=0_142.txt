
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3,8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other # the "other" tensor is passed as a keyword argument to the addition operation 
        return v2


# Initializing the model and setting the `other` tensor value. 
m  = Model()

other  = torch.tensor([0., .5, .7071067811865476]) # This is a dummy vector for illustration purpose only.  Please use a meaningful other value.
m(x1)

