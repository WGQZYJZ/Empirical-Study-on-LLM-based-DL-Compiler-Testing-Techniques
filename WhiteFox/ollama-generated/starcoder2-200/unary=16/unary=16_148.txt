
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(640*3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = F.relu(v1)
        return v2


# Initializing the model
m  = Model2()

# Inputs to the model
x1  = torch.randn(10,64*3) # Randomly sampled input tensor of size (10, 576).
