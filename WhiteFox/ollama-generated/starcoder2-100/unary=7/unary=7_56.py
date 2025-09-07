
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(784, 600, bias=False)

    def forward(self, x):
        l2 = self.l1(x)
        l3 = F.elu(F.dropout(clamp(min=-3), p=.5))
        return (l2 + 3).clamp(-3., -7.).div_(6.)


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 784)
