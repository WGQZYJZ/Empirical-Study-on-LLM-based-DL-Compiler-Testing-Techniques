
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, input1, inp): # 'input1' and 'input2' are the two tensors to be multiplied. 'inp' is another tensor passed as a keyword argument which is to be added to the result of matrix multiplication.
        v1 = torch.mm(input1, input2) 
        return  v1 + inp


# Initializing the model
m  = Model()

# Inputs for the model
x1  = torch.randn([3,4]) # A 5-by-6 matrix. These are to be passed as two input tensors to 'mm' function in PyTorch.
x2 = torch.randn([4,7])
inp = torch.randn(3) 

__output___ = m(x1, x2 , inp=inp)

