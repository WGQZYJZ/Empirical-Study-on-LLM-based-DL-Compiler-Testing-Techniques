
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.permute(x1, [0, 2, 1]) # Permute the input tensor
        v2  = torch.nn.functional.linear(v1)
# Initialize the model m
m = Model()
# Input tensors to the model
x1 = torch.randn(3, 5) # Any valid input for the Model class will suffice


