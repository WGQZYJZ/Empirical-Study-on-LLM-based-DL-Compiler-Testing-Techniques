
class Model(torch.nn.Module):
    def __init__(self, n: int):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.dense1 = torch.nn.Linear(5 * 64 + 7, 30) 
        self.dense2 = torch.nn.Linear(30, n)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2 = torch.flatten(v1, start_dim=1)
        v5  = self.dense1(v2) 
        v6  = self.dense2(v5)
        return v6


# Initializing the model
m = Model(43)

# Inputs to the model
x1 = torch.randn(8, 3, 70, 90) # Assuming the input size is 3 x 70 x 90
