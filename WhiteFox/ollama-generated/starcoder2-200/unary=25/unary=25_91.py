
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         t2  = torch.zeros([3,4], dtype=float)
         for i in range(x1.shape[0]):
            for j in range(x1.shape[1]):
                t5 = torch.where((x1[i][j] < 7), x1[i][j] * -0.2 + 5, x1[i][j])
         return t5


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(43, 6) 
 __output__  = m(x1)