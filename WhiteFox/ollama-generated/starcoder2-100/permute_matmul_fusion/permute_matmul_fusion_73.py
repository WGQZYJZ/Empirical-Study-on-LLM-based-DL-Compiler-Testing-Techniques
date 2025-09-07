
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x1):
         v1  = x1 .permute(0, 2 ,1) # A_P
         v3  = torch.bmm(v1,  input_tensor_B).permute(0, 3, 2 ,1 )
         return self.linear(v3)


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 4, 5)
