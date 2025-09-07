
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, x2):
        v1  = input_tensor_A.permute(...) # or t1 = input_tensor_B.permute(...) # or t2 = input_tensor_C.permute(...) # or t3 = torch.bmm(t1, t2)
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 2)
x2 = torch.randn(1, 2, 3)
