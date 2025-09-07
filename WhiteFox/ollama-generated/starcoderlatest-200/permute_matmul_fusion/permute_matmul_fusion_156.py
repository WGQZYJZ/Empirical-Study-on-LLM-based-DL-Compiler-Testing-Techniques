
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2=None):
        v1 = input_tensor_A.permute(...) # Permute the first tensor
        v2 = input_tensor_B.permute(...) # Permute the second tensor
        t3 = torch.bmm(v1, v2)  # or torch.matmul(t1, t2)

        if x2 is not None:
            v3 = torch.nn.functional.linear(t3, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted tensor
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
if x2 is not None:
    x2 = torch.randn(1, 2, 2)
