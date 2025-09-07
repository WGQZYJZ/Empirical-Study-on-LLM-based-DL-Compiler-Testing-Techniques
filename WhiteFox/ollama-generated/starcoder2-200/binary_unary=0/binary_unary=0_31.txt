
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2  = torch.nn.Conv2d(3, 4, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + other_tensor()
        v3  = torch.relu(v2)
        v4  = self.conv2(x)
        return v4


# Initializing the model and generating inputs
m,  x  = generate_model() # m is an instance of Model class; x1, x2 are two randomly generated inputs to the model
 