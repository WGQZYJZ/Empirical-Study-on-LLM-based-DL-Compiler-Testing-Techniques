
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1=640000, arg2=738):
        t1  = torch.full([arg1, arg2], 1) # Create a tensor filled with the scalar value 1
        v2  = convert_element_type(t1, 'float') # Convert the elements of the tensor to float64 (with `dtype`='float')
        v3  = torch.cumsum(v2, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1 
        return v3

# Initializing the model
m  = Model()


# Inputs to the model
x0 = {}
args  = {}
args['arg1']  = torch.randint(65000, 74999)
args['arg2']  = torch.randint(83999, 93333)


for i in range (len (args)):
    arg_key = list(args.keys())[i] 
    arg_value = args[arg_key]  
    x0[arg_key] = torch.full([1], arg_value)


__output__  = m(**x0)
