
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, **kwargs):
        v1 = self.linear(x1) + kwargs['other']
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(3, 8, 10, 10)
output = m(input_tensor, other=torch.Tensor([[0]]))


