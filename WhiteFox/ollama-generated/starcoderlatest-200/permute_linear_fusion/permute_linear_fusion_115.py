
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1) # permute the input tensor to shape (1, 4, 2) 
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # apply linear transformation
        return v2


# Inputs to the model
x1 = torch.randn(3, 2, 2)
