
class Model(torch.nn.Module):
    def __init__(self, num_inputs: int=10, num_outputs: int=5):
        super().__init__()
        self.linear = torch.nn.Linear(num_inputs, num_outputs)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float()
        v3 = (v1 * -0.0078431372549019607).float()
        v4 = torch.where(v2, v1, v3)
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 10, 512, 512)
