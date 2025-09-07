
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 38)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor 
        v3 = F.relu(v2)
        return v3

# Initializing the model and passing the tensor to be added later on
m  = Model()
other_tensor  = torch.randn(1024, 38)
 
# Inputs to the model
x1  = torch.randn(576, 1024)
