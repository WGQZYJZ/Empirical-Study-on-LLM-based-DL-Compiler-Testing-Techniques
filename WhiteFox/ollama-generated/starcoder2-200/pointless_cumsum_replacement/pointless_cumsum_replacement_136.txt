
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1):
        t2  = torch.full([arg1, 8], 3) 
        t5  = torch.ones(t2.shape).int() 
        t6  = t4 * 0.7071067811865476 
        t7  = torch.nn.LeakyReLU()(t5, negative_slope=t3)
        return t6

# Initializing the model
m  = Model() 

# Inputs to the model
input2  = torch.randint(0, 8, [1]) # Please input a tensor with one integer element
input4  = torch.ones([5], dtype=torch.int)

 __output__  = m(input4)
