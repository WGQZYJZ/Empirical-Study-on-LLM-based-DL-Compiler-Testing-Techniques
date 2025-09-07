
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
         t1  = torch.mm(input1, input2)
         t2  = torch.cat([t1] * 4, dim=0)
         return t2

# Initializing the model
m  = Model()
 
__inputs_list__ = [
    (torch.randn(32),
     torch.randn(5)),
 
    (torch.randn(96),
     torch.randn(18))]
 
# The output is obtained after passing different input values to the model
for t in __inputs_list__: 
    __output__  = m(*t)

