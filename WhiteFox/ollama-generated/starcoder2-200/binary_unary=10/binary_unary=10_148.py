
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2)
        return v3


# Initializing the model
m = Model()
 
other_tensor  = torch.randn(10, 64).to('cuda')
# Inputs to the model on GPU:
x1  = torch.randn(10, 32, requires_grad=True).to('cuda')
# Predicted output values of the model from GPU inputs x1 on CPU: 
__output__  = m(x1)

