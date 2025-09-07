
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1  = torch.permute(x1, [0, 3, 2])
        t1a  = self._compute_t1a_(x1) # Some custom op/module which uses permute internally to swap dimensions

        t2a  = self._compute_t2a_(x2) # Some custom op/module which uses permute internally to swap dimensions
        
        t3  = torch.bmm(t1, x2)
        t4  = torch.bmm(t1a, t2a)

        return t3 + t4

m  = Model()

