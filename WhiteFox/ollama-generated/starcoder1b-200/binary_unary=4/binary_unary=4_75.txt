
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x):
        v = self.linear(x)
        other = torch.tensor([[1], [2], [3]], requires_grad=True)
        return relu(v + other)


# Inputs to the model
input_tensor = ... # An input tensor
__output__  = Model()(input_tensor)

