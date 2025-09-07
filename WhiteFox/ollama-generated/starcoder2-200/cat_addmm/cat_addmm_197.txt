
class Model(torch.nn.Module):
    def __init__(self, mat1=None, mat2=None):
        super().__init__()
 
    def forward(self, input):
        t1 = torch.addmm(input, mat1, mat2)  # Add matrix multiplication of mat1 and mat2 to the input tensor
        t2 = torch.cat([t1], -3)  # Concatenate along axis with size 3
        return t2

# Initializing model for generating an output
model_out = Model()
 
input  = torch.randn(4,8,60)
model = Model().cuda()
model.load_state_dict(torch.load("output_model/checkpoint-79500.pt"))
__output__  = model(input).cpu().detach()

