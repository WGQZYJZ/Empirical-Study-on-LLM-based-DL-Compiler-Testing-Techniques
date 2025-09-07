
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(64*64*3, 512)
    def forward(self, x):
        v0  = x 
        v1  = conv(x1)
        v2  = linear(v1)
        v3  = sigmoid(v2) # Sigmoid
        return v0 * v3
 

