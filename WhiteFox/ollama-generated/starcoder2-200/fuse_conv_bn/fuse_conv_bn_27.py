
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 50)

    def forward(self, x1):
         v1 = torch.nn.functional.relu(self.conv1(x1))

         v2 = torch.nn.functional.batch_norm(v1)
         return v2

model = Model()


# Initializing the model
output  = m(torch.randn(50, 3, 496, 872))

# Inputs to the model
x1 = torch.randn(50, 3, 496, 872)