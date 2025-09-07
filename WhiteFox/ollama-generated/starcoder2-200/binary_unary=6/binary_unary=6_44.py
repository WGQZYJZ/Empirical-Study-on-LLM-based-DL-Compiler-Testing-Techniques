
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 8)
        self.other = 13.4675779
    
    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 - self.other
        v3  = F.relu(v2)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
    x = torch.randn(5, 20).requires_grad_()
