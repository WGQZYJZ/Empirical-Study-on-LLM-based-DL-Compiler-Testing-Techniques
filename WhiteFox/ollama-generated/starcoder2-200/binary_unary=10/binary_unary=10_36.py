
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.lin  = torch.nn.Linear(1024, 1)
 
    def forward(self, x1):

        v5 = self.lin(x1).float() + other  # pylint: disable=undefined-variable
        v6 = torch.relu(v5)  # pylint: disable=undefined-variable
        return v6
# Initializing the model
m  = Model()
 
# Input to the model
x1 = torch.randn(4, 256 * 8 * 8).requires_grad_(True) # [batch size, features]
__output__  = m(x1)

