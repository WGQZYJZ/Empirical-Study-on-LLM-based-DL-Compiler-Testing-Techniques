
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.ops.aten.matmul()
 
    def forward(self, input1, input2, inp):
        v1  = self.mm(input1, input2) # The 'mm' operation is called here in the forward pass.
        v2  = v1 + inp                 # 'v1' is a variable of the first 'mm' operation.
        return v2

# Initializing the model
m = Model()

