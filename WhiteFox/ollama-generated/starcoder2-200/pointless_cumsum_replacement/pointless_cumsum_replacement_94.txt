
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1 = torch.full([arg1, arg2], 1)
        v2 = v1.to(dtype=dtype) 
        v3 = v2.cumsum(dim=1)  
        return v3


# Initializing the model
m = Model()


# Inputs to the model
__arg1__, __arg2__, dtype, layout, device  = 64, 'int', 0, torch.__layout__.C, 'cuda'
input_dict = {
    "__arg1__": torch.tensor(__arg1__),
    "__arg2__": torch.tensor(__arg2__)
}

 # Run the model and get the output
m(**input_dict)