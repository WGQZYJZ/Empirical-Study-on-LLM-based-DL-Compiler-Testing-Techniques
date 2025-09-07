
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1):  # input 3 matrices with shape [m*256, n] each
        t0 = torch.mm(x1,y1)
        t1 = torch.mm(z1,t0) + t0
        return t1

# Initializing the model
m = Model()

 # Inputs to the model 
x1  = torch.randn([64*256, 78], requires_grad=True).to('cuda')
y1  = torch.randn([64*256, 30], requires_grad=True).to('cuda')
z1  = torch.randn([78*30, 98]).to('cuda')

 # Model outputs and grads 
__output__ , __grad_output__   = m(x1, y1, z1)

