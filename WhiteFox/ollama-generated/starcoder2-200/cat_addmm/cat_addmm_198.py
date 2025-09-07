
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()

        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 16, 1)

    def forward(self, x):
        
        v1 = conv1(x) 
        v2 = conv2(v1)
        v4 = torch.addmm(x, mat_a, mat_b) # 1
        v5 = t1(conv3(t2)) # 2
        v7 = v6 + 1.0

        return [v1, v2]


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 48, 48)
