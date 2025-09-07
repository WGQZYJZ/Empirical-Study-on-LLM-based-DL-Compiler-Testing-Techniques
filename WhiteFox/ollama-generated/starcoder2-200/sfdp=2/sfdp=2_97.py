

class Model(torch.nn.Module):
    def __init__(self, hidden_dim1=32, hidden_dim2=8):
        super().__init__()

        self.linear1 = torch.nn.Linear(hidden_dim1*3 + 1, hidden_dim2)
        self.linear2 = torch.nn.Linear(hidden_dim2+100, 500)
        self.relu   = torch.nn.ReLU()

    def forward(self, x1):

        # The inputs are: [x1, 1] (for the first layer), [x3, x4, ...x18] 
        # (for the subsequent layers after the first).
        v1_firstLayer = self.linear1(torch.cat([x1, torch.tensor(1.0)], dim=0))
        v2_firstLayer = self.relu(v1_firstLayer)
        
        v3  = self.linear2(
            torch.cat([
                v2_firstLayer, 
                x3 + x4 + ... + x18
            ], dim=-1).div(inv_scale_factor)
        )
        return v3


m = Model()
