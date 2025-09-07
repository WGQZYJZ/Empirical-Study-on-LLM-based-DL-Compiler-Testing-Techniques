
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t1 = torch.full([arg1, arg2], 1)
        t2 = convert_element_type(t1, dtype=dtype)
        t3 = torch.cumsum(t2, dim=1) 
        return t3

# Initializing the model and printing its arguments' name-value pair with its arguments
m  = Model()
for name , val in m._modules['forward'].named_parameters():
    print(name , val)
    
arg1  torch.Size([8, 9])
arg2  5

