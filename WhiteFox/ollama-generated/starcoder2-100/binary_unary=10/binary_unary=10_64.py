
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64*3, 256)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = v1 + other_tensor 
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()

 # Inputs to the model 
other_tensor = torch.randn(5, 4096).cuda()
 
x1 = torch.randn(2, 3, 64, 64).cuda()
