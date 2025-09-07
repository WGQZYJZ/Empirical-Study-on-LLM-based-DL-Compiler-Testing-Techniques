
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)
        return v1 + other
 
 
 # Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(56, 320)
other = torch.randn(320).view(-1, 1).expand_as(x1[:, :-1])
 
  # Generating the inputs for the output model
  __input__ = torch.cat([other] + [torch.randn(57, x1[:, i].shape[-1]).view(-1, 1)
                                   for i in range(x1.shape[1])], -1).view_as(x1).detach()

 