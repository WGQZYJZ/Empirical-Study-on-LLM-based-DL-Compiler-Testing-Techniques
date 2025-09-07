
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 128)

    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor
        return relu_(v1)


# Initializing the model
m  = Model()


other_tensor = torch.randn(5, 64).requires_grad_() # Dummy tensor to be passed as keyword argument in `Model.forward` method.

# Inputs to the model
x1 = torch.randn(10, 32)

