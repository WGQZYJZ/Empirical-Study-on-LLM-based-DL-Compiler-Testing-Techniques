
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):

        v1  = x1.permute(0, 2, 1).reshape(-1, 2)

        return torch.nn.functional.softmax(v1 @ self.linear.weight + self.linear.bias)

# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(50, 3 , 4)
 __output__  = m(x1).sum(-1)

 