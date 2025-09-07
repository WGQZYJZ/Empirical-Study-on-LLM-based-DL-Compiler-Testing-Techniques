
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
         # t1  = x1.permute(...).unsqueeze(0)
         v1  = torch.bmm(x2, self.linear.weight + 5)
        return v1


# Initializing the model
m = Model()

# Inputs to the model