
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.BMM()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permutes the input tensor A
        v2 = x2.permute(0, 2, 1) # Permutes the input tensor B
        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        v4 = torch.nn.functional.linear(v2, v3, self.linear.bias)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 2, 2)
x2  = torch.randn(1, 2, 2)
