
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2) 
        v3  = v1 + input2 # Add 'inp' tensor to the result of matrix multiplication
        return v3

# Initializing the model