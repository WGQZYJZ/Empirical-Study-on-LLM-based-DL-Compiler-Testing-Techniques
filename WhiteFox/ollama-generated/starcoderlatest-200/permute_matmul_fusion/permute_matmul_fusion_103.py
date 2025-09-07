
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.nn.functional.linear(x1, self.linear.weight) # or torch.matmul(t1, t2)
        v2 = torch.bmm(v1, x2) # or torch.matmul(input_tensor_A, input_tensor_B)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 4)
x2 = torch.randn(3, 5, 6)
