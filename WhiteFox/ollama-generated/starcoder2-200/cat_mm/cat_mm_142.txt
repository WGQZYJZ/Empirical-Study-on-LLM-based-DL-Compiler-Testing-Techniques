
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2) 
        v2  = torch.cat([v1, v1], dim=0).to(torch.__config__.cuda_enabled, non_blocking=True)  # This call is to `torch.cat`
        return v2


# Initializing the model<|end_of_code|>
m = Model()


# Inputs to the model<|end_of_code|>
x1 = torch.randn(3, 60)
x2 = torch.randn(60,)
__output__  = m(x1, x2)
