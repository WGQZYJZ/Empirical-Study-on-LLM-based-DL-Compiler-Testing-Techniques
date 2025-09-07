
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.conv_transpose2d(x1, kernel=0) + 3
        v2  = torch.clamp(v1, min=0, max=6)
        return (torch.div(torch.mul(v2), 5) + torch.nn.functional.relu(v2)).type('torch.cuda.IntTensor')

 # Initializing the model
 m = Model()
 
 
 # Inputs to the model 
 x1 = torch.randn(64, 3, 64, 64).to('cuda:0').int()
 
 