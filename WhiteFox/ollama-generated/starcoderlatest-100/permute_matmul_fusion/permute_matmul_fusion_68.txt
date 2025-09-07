
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2) # or torch.matmul(input_tensor_A, input_tensor_B)
        v2 = v1.permute(...)   # Permute the main input tensor after invoking the batch matrix multiplication function.
        return self.linear(v2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 3)
x2 = torch.randn(3, 4, 5)
