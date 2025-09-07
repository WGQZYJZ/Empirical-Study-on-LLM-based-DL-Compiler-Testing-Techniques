
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q  = torch.nn.Parameter(torch.zeros((3,)))
        self.k1  = torch.nn.Linear(80, 4)
        self.k2  = torch.nn.Linear(75, 6)
 
    def forward(self):
        v1  = (
            torch.matmul(
                query=torch.nn.functional.dropout(x, p=0.3), 
                key=torch.nn.functional.dropout(y, p=0.4))
            + self.k2(z)).relu()

        v2  = k1(v)
        return v2 * v3


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.zeros((75,))
k1, k2 = torch.nn.Linear(80,4), torch.nn.Linear(75,6)  # Note that these are not parameters of our model
x, y, z  = torch.randn(3, 80), torch.randn(5, 75), torch.zeros((9, 1))
__output__  = m()

