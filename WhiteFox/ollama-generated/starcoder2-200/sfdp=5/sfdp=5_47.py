
class Model(torch.nn.Module):
    def __init__(self, nk=4096):
        super().__init__()
 
        self.conv1 = torch.nn.Conv2d(384*3+512, 3 * nk , 1)
 
        self.mlp_h = torch.nn.Sequential(*[
            torch.nn.LayerNorm(),
            torch.nn.Linear(nk),
            torch.nn.GELU()
        ])
 
        self.mlp_q = torch.nn.Sequential(*[
            torch.nn.LayerNorm(),
            torch.nn.Linear(nk),
            torch.nn.GELU()
        ])
 
    def forward(self, query):
        # query 4D tensor
        keys = []
        for idx in range(query.size(1)):
            conv_in = query[:,idx]
            keys.append(self.conv1(conv_in))
 
        # stacking 4D tensors into 3D tensor
        keys = torch.cat(keys, dim=0).view(-1, nk)
 
        # apply mlp to 2D
        keys = self.mlp_h(keys)
 
        # computing dot product between query and keys
        keys = self.mlp_q(query @ keys / math.sqrt(query.size(-1)))
 
        return keys
# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4,387*3+512) # Size 4, 196 000
x2 = torch.randn(3, nk) # Size: 196 000


