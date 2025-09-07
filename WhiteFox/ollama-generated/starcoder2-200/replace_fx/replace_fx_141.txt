
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)
        self.drop1   = torch.nn.Dropout(p=0.5)

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, p=0.4)
        v2  = torch.rand_like(v1) 
        return self.linear(v1), v2


# Initializing the model
m = Model()

# Inputs to the model
input_tensor  = torch.randn(1, 2)
__output__   = m(input_tensor).sum(),