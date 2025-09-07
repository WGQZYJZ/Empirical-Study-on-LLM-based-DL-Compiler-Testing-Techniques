
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1 = torch.nn.Linear(320, 5)  # Linear transformation with 320 inputs and 5 outputs.
        v2 = torch.sigmoid(v1(x))  # Sigmoid function applied to the output of the linear transformation.
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x_tensor = torch.randn(3, 320)
