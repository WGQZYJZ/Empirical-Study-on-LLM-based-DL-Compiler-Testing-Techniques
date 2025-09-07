
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 84, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()
m.cuda() # Making sure that model is on GPU
 
# Inputs to the model
x1  = torch.randn(4, 32 * 84).cuda()
other_tensor  = torch.ones(v1.shape[0], v1.shape[-1]).cuda()

__output__  = m(x1)

# Input tensor to the model
__input__  = [x1, other_tensor]