
class Model(torch.nn.Module):
    def __init__(self, feat_size):
        super().__init__()
        self.fc = torch.nn.Linear(feat_size, feat_size)
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x2, x2)
        v2 = self.fc(v1)
        return v2


# Initializing the model
m  = Model(32)

