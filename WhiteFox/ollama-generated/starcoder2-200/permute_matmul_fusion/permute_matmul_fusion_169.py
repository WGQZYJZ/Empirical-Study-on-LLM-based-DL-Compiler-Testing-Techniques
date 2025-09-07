
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(2, 4)
        self.linear2  = torch.nn.Linear(4, 3)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # Permute the input tensor
        v2  = torch.bmm(v1, self.linear1.weight).add_(self.linear1.bias)

        return torch.nn.functional.relu(
            v2.matmul(self.linear2.weight)) + \
               self.linear2.bias


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 4)
  __output__  = m(x1)
  
