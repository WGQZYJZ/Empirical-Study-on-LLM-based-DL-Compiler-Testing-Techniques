
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
         t3  = torch.bmm(x1.permute(...), x2) # or torch.matmul(input_tensor_A, t1)


# Initializing the model
m = Model()

# Inputs to the model
__inputs__= torch.randn(3, 50), 150)

# Running the model and getting the output
