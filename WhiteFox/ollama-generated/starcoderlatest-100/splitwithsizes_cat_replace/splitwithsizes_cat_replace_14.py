
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split = torch.split(input_tensor, 3, dim=1)
 
    def forward(self, x1):
        v1 = self.split[0]
        v2 = self.split[1]
        return v1 + v2


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
