
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(7, 5)
        self.softmax = torch.nn.Softmax()
 
    def forward(self, x1):
        v1  = self.matmul(x1)
        v2  = v1 * inv_scale_factor 
        v3  = self.softmax(v2)
        v4  = v3 + dropout_p
        v5  = torch.nn.functional.dropout(v4, p=0.)
        v6  = v1.matmul(value)

        return v6

# Initializing the model
m = Model()
# Inputs to the model
x1  = torch.randn(7)

 # Please add dropout here
__output__  = m(x1)

