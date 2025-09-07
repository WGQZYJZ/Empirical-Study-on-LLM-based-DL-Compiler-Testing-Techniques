
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor  # <--- This is a new tensor that was not used in the previous example
        v3  = torch.nn.functional.relu(v2)
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 1024) # This is a different input tensor than in the previous example.


# The output of the model for the previous example:
y_1 = m(x1)

