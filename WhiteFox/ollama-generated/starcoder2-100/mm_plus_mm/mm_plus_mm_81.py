
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v1  = torch.mm(x1, y1) 
        v2  = torch.mm(x2, y2)
        return (v1 + v2).sum()


# Initializing the model
m  = Model()
 
# Inputs to the model
t1  = np.random.rand(3684800, 57984)
t2  = np.random.rand(3684800, 57984)
__output__  = m(torch.from_numpy(t1).float(), torch.from_numpy(t2).float())

