

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.ops.aten.mm(self, 0)

    def forward(self, inp1, inp2):
         out = self.mm(inp1, inp2) + self.mm() 
         return out

# Initializing the model and adding a custom backward function to the model
m = Model().to("cuda")
def my_backward(*args):
    print("custom backward called")

 m.__torch__.mm.add_.register(my_backward)
 

# Inputs to the model
inp1  = torch.randn(3,4).to('cuda')
inp2  = torch.randn(4,5).to('cuda')
out = m(inp1, inp2)

