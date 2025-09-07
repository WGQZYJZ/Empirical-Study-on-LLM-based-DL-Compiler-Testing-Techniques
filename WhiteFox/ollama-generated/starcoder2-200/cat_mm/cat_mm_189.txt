
class Model(torch.nn.Module):
    def __init__(self, m):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)  # Matrix multiplication of two input tensors
        v2 = torch.cat([v1] * len(m), dim=0)  # Concatenation of the result tensor along a certain dimension
        return v2


# Initializing the model
m = torch.nn.ParameterList(
    [torch.ones((3,)), torch.zeros((4,))], requires_grad=True
)
 
m1  = Model(m)
__output__  = m1(x1, x2)

