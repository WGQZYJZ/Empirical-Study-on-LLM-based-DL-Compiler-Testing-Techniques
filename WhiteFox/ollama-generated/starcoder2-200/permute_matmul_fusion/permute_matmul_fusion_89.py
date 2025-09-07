
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.bmm(x1,  x2) # or torch.matmul(input_tensor_A, t1)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 4 , 5 )  
x2  = torch.randn(3, 5, 7 )  


__output__  = m(x1, x2)



