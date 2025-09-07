
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1):
        v0  = torch.zeros([256], dtype=torch.float32)
        v1  = self._myfunc(x1,y1,v0)
        v2  = self._myfunc(x1+1,y1+1,v1) + x1  # Adding the result of matrix multiplication to the input value
        return v2


# Initializing the model
m  = Model()

