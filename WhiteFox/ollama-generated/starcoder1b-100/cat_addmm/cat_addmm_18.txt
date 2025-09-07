
class Model(torch.nn.Module):
    def __init__(self, feature_dim, label_dim):
        super().__init__()
        self.feature_dim  = feature_dim
        self.label_dim  = label_dim
 
    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        w1 = torch.mm(v1, torch.ones((v1.shape[0], self.feature_dim)))
        b1  = torch.zeros((w1.shape[0], 1))
        o1 = torch.addmm(w1, x1, b1)
        w2 = torch.cat([torch.ones((1, self.label_dim)), x2], dim=0)
        w3 = torch.mm(w2, torch.ones((self.label_dim, 1)))
        b2  = torch.zeros((w3.shape[0], 1))
        o2 = torch.addmm(w3, x2, b2)
        return o1 + o2


# Initializing the model
m = Model(feature_dim=3, label_dim=4)

