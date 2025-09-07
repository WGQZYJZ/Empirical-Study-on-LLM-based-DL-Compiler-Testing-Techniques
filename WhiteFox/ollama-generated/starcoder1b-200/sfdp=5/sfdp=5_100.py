
class Model(torch.nn.Module):
    def __init__(self, model_name):
        super().__init__()
        self.model = model_name
 
    def forward(self, x1):
        v1  = self.model(x1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
