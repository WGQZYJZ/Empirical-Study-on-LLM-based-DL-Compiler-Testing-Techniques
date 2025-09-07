
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1:torch.Tensor, y1:torch.Tensor, x2:torch.Tensor, y2:torch.Tensor) -> torch.Tensor:
        v1 =  torch.mm(x1,y1)
        v2 =  torch.mm(x2,y2)
        v3 = v1 +v2

# Initializing the model
m = Model()


# Inputs to the model
x1=torch.randn(3072 ,512 )
y1=torch.randn(512 , 64)
x2=torch.randn(3072, 512)
y2=torch.randn(512 , 64)
