
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3*64, 8)

    def forward(self, x1):
        return self.linear1(x1).sub(-other_value)


# Initializing the model
m = Model()
print('The parameters in the model:')
for name_, param in m.named_parameters():
    print(name_, ' ', end='')
    for i in param:
            print(i, ',')
# Inputs to the model
x1  = torch.randn(1, 3*64)


