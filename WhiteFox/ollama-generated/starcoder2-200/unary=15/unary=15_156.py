

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
#         v2  = v1 + 1 # uncomment this line to trigger the error
#         return v1 * v2 # uncomment this line to trigger the error
        v3 = torch.relu(v1) # add ReLU activation function 
        return v3

