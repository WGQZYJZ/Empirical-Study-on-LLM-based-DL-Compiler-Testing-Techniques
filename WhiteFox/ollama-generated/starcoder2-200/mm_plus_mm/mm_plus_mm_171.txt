
class Model(torch.nn.Module):
    def __init__(self, input1, input2, input3, input4):
        super().__init__()
        self.matmul  = torch.nn.Linear(input1 * input2, input3 * input4)
 
    def forward(self, x1, x2): 
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(v1, 0)
        return self.matmul(v2)

# Initializing the model
input_shape  = [49578] + 4 * [(32,) ]
m  = Model(*input_shape)

 # Inputs to the model
torch.manual_seed(1336084807)

x1  = torch.randn(1, input_shape[0])
__output__  = m(x1, x2)
