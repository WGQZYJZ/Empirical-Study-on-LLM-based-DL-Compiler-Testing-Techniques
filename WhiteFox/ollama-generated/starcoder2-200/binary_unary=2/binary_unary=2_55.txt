
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        v3  = F.relu(v2) # Replace F with torch (or torch.*), it is okay!
        return v3


# Initializing the model and passing the 'other' tensor to the model, or you may do it any way that would make your program correct.
m  = Model()
other  = ... 
__output__  = m(x1)

