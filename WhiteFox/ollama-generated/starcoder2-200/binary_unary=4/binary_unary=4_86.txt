
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 3072)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2)
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
__init_input__ = torch.randn(1, 6400)
other_tensor  = torch.rand(1, 897)
__output__   = m(__init_input__)