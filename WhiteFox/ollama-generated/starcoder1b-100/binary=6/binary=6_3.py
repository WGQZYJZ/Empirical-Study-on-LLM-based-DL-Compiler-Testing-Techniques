
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.5
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32, requires_grad=True)
v1 = m(x1)
v2 = m(x1) - 0.5
grads.append(m.named_parameters())
print(grads[-1][1].grad)
# [None]

