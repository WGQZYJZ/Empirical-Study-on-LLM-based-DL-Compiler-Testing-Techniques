
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
         v1  = torch.mm(x1, x2)
         v2  = torch.mm(x3, x4)
         return v1 + v2


# Initializing the model
m  = Model()
input_x1  = torch.randn([56, 78])
input_x2  = torch.randn([78, 90])
input_x3  = torch.randn([56, 78])
input_x4  = torch.randn([78, 90])

 # Model output
output__  = m(input_x1, input_x2, input_x3, input_x4)

