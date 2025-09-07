
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1  = x1 .permute(0, 2, 3) 
        t2  = torch.nn.functional.linear(t1, self.linear.weight, self.linear.bias)
        return t2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 5).permute(0, 2, 1) # input_tensor_A
x2 = torch.randn(4, 5, 7).permute(0, 1, 2) # input_tensor_B


__output__  = m(x1)(x2)