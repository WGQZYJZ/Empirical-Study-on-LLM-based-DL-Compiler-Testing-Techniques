
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1


# Initializing the model
m  = Model()


# Inputs to the model: The input tensor will be different from the previous one.
x1_1  = torch.randn(32, 8)
x1_2  = torch.randn(34, 5)
x1_3  = torch.randn(9, 7)


# Model's output: The model will generate an additional tensor `v2` with the same shape as a linear transformation is applied to the input tensors. But the output of applying ReLU on it should be different from the previous one.
v1_1 = m(x1_1)
v1_2 = m(x1_2)  # Generate a tensor v1 with the same shape as a linear transformation is applied to another input tensor `x2`, but the output of applying ReLU on it should be different from the previous one.
v1_3 = m(x1_3)

