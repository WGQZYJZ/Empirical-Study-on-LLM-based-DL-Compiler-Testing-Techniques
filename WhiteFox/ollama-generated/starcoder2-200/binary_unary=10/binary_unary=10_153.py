
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor 
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Input tensor to the model
x1  = torch.randn(64, 1024).to(device=torch.device("cuda"), dtype=torch.float32)
other_tensor = torch.zeros(128, 3, device="cuda", dtype=torch.float32)
__output__  = m(x1)
