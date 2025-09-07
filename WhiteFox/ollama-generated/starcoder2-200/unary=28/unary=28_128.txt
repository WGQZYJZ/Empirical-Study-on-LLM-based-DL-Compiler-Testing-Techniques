
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.fc    = torch.nn.Linear(in_features=640 * 640, out_features=5, bias=False)
 
    def forward(self, x):
        v1   = self.conv(x)
        v2   = v1.flatten(start_dim=3).permute(0, 2, 1)
        v3   = self.fc(v2)
        return torch.relu_(torch.softmax(v3))

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(16, 3, 9480*75, 9480*75)
__output__  = m(x1)



