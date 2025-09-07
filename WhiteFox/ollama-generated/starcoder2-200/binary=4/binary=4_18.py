
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3,4)

    def forward(self, x1):
        v1  = self.linear(x1) + torch.randn(1, 4, dtype=torch.float64).to("cuda")
        return v1


# Initializing the model and loading weights into it.
m2 = Model2()
state_dict = torch.load('weights.pt')
m2.load_state_dict(state_dict)
m2.eval()


# Inputs to the model
x2  = torch.randn(1, 3).to("cuda")
__output___ = m2(x2)

