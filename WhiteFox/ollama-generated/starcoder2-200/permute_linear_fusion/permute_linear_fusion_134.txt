
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1):
       v1 = x1[:, :, 0] + x1[:, :, -1:]
	v2 = torch.nn.functional.relu(v1.clone())
	v3 = self.linear(x1)
       return v2, v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(40, 20 ,5, 28).detach().requires_grad_()


