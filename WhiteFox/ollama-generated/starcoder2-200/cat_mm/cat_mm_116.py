
class Model(torch.nn.Module):
    def __init__(self, num_tensors):
        super().__init__()
        self.num_tensors = num_tensors
 
    def forward(self, inputs):
        v1  = torch.mm(inputs[0], inputs[1])
        v2  = torch.cat([v1 for i in range(3)], dim=0)
        return [v2]

# Initializing the model
m  = Model(num_tensors=2).cuda()
 
# Inputs to the model
x1, x2  = torch.randn(64, 78), torch.randn(78, 93).cuda()
 
inputs = [x1, x2]
__output__  = m(*inputs)

