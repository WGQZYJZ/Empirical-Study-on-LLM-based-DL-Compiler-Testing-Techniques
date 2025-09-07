
class Model(torch.nn.Module):
    def __init__(self, n=1024):
        super().__init__()
 
        self.layer = torch.nn.Linear(n*8+3*512 + 512*20, n)
 
    def forward(self, x):
        t_296  = torch.nn.functional.linear(x, self.layer.weight.t())
        t_297  = torch.cat([torch.nn.functional.relu(torch.sigmoid(f)) for f in torch.split(
            t_296, [80], dim=1)], 1) + x
        t_295  = self.layer(t_297).sum()
 
        return  t_295

# Initializing the model
m  = Model()
 
# Inputs to the model