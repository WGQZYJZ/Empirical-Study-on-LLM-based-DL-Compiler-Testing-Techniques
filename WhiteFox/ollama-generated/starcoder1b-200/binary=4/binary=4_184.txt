
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other  # Add another tensor to the output of the linear transformation
        return v1


# Inputs to the model
input_tensor = torch.randn(2, 10)
other = torch.randn(2, 5)
