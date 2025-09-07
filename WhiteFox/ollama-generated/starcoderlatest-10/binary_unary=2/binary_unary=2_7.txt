
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other_t3 = torch.rand([8], requires_grad=True).to(dtype=torch.float64)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - self.other_t3
        v3 = torch.nn.functional.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn([1, 3, 64, 64])
