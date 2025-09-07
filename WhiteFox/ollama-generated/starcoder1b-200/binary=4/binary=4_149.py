
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 10)
 
    def forward(self, x):
        return self.linear(x) + other  # Add another tensor to the output of the linear transformation


# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(5, 128)
